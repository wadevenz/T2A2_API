from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import bcrypt, db
from models.user import User, user_schema, users_schema, UserSchema


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        body_data = request.get_json()
        
        user = User(
            name=body_data.get("name"),
            email=body_data.get("email")
        )

        password=body_data.get("password")

        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return{"error": "Email address already in use"}, 409

@auth_bp.route("/login", methods=["POST"])
def login_user():
    body_data = request.get_json()
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)

    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):

        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))

        return {"email": user.email, "is_admin": user.is_admin, "token": token}
    
    else:
        return {"error": "Invalid email or password"}, 401
    
@auth_bp.route("/users")
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return users_schema.dump(users)

@auth_bp.route("/users/<int:users_id>", methods=["DELETE"])
def delete_user(users_id):
    stmt = db.select(User).filter_by(id=users_id)
    user = db.session.scalar(stmt)

    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User with id '{users_id}' has been deleted"}
    else:
        return {"error": f"User with id '{users_id}' does not exist"}

@auth_bp.route("/users", methods=["PUT", "PATCH"])
@jwt_required()
def update_user():
    body_data = UserSchema().load(request.get_json())
    password = body_data.get("password")
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    if user:

        user.name = body_data.get("name") or user.name
        user.email = body_data.get("email") or user.email
    
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
        
        db.session.commit()

        return user_schema.dump(user)

    else:
        return {"error": "User does not exist"}