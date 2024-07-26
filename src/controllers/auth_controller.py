from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import bcrypt, db
from models.user import User, user_schema, users_schema, UserSchema
from utils import auth_as_admin_decorator

# Creating a blueprint for the auth controller and creating a universal prefix for below routes. 
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Route to register a new user via POST method. 
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        # Request the data from the JSON body.
        body_data = UserSchema().load(request.get_json())
        
        # Create an instance of the user using the User model.
        user = User(
            # Attribute information retrieved from requested JSON body data.
            name=body_data.get("name"),
            email=body_data.get("email")
        )
        password=body_data.get("password")

        # Checks if password is given and utilises bcrypt library to hash password.
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Add the user to the session.
        db.session.add(user)
        # Commit the session.
        db.session.commit()

        # returns the registered user.
        return user_schema.dump(user), 201
    
    # try/except block to enable the handling of integrity errors in the case of Integrity errors.
    # Not nullable fields must have input and email inputs must be unique.
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return{"error": "Email address already in use"}, 409

# Route to enable a user to login.
@auth_bp.route("/login", methods=["POST"])
def login_user():
    # Request the data from the JSON body.
    body_data = request.get_json()
    # Find the user in the database where the email matches the one given in the JSON body.
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)

    # If the user exists, utilise bcrypt library to hash the password given, and check
    # the hashed password matches the user retrieved from the databse. 
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # Creating a JWT for the user.
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # returns user information including JWT.
        return {"name": user.name, "email": user.email, "is_admin": user.is_admin, "token": token}
    # If user does not exist return error message.
    else:
        return {"error": "Invalid email or password"}, 401

# Route to retrieve all users.
@auth_bp.route("/users")
# Valid token required from a logged in user.
@jwt_required()
# Use decorator to check if user is admin. 
@auth_as_admin_decorator
def get_users():
    # Retrieve all users from the database.
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    # returns users.
    return users_schema.dump(users)

# Route to delete user.
@auth_bp.route("/users", methods=["DELETE"])
# Valid token required from a logged in user.
@jwt_required()
def delete_user():
    try:
        # Retrieves the user where the id matches the logged in user via the valid JWT.
        stmt = db.select(User).filter_by(id=get_jwt_identity())
        user = db.session.scalar(stmt)
        if user:
            # Delete the user.
            db.session.delete(user)
            # Commit the session.
            db.session.commit()
            # Return a success message
            return {"message": f"User with id '{user.id}' has been deleted"}
        else:
            return {"error": f" User with id '{user.id}'does not exist"}
    except AttributeError as err:
        return {"error": "User not found"}, 404
    
# Route to update a user.
@auth_bp.route("/users", methods=["PUT", "PATCH"])
# Valid token required from a logged in user.
@jwt_required()
def update_user():
    # Retrieves the data from the JSON body using UserSchema to aid deserialisation.
    body_data = UserSchema().load(request.get_json())
    # If password given, retrieve password from JSON body.
    password = body_data.get("password")
     # Retrieves the user where the id matches the logged in user via the valid JWT.
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    # If user exists update fields with retrieved body data or maintain current value.
    if user:

        user.name = body_data.get("name") or user.name
        user.email = body_data.get("email") or user.email

        # If password given, use bcrypt to hash the password.
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        
        # Commit the session.
        db.session.commit()

        # Return the user.
        return user_schema.dump(user)
    
    # If user does not exist return error message. 
    else:
        return {"error": "User does not exist"}