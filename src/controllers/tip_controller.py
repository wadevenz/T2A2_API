from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.tip import Tip, tip_schema, tips_schema
from models.match import Match
from models.user import User

tips_bp = Blueprint("tips", __name__, url_prefix="/tips")

# Route to get all tips from the database.
@tips_bp.route("/")
# Check for a valid web token.
@jwt_required()
def get_all_tips():
    # Fetch all tips from the database.
    stmt = db.select(Tip)
    tips = db.session.scalars(stmt)
    # Return the tips to the database. 
    return tips_schema.dump(tips)

# Route to get a single tip from the database. 
@tips_bp.route("/<int:tip_id>")
# Check for a valid token.
@jwt_required()
def get_one_tip(tip_id):
    # Fetch single tip from database based on comparing id to tip_id from the route.
    stmt = db.select(Tip).filter_by(id=tip_id)
    tip = db.session.scalar(stmt)
    # If the tip exists, return the tip to the user.
    if tip:
        return tip_schema.dump(tip)
    # If the tip does not exist, return an error message.
    else:
        return {"error": f"Could not locate tip with id {tip_id}"}, 404

# Route to create a tip.
@tips_bp.route("/", methods=["POST"])
# Check for a valid JWT.
@jwt_required()
def create_tip():
    # Get JSON data from the body of the request. 
    body_data = tip_schema.load(request.get_json())
    
    # Create a tip instance. 
    tip = Tip(
        selection=body_data.get("selection"),
        user_id=get_jwt_identity(),
        match_id=body_data.get("match_id")
    )
    # Fetch the match from the tip, where the match id coresponds.
    stmt = db.select(Match).filter_by(id=body_data.get("match_id"))
    match = db.session.scalar(stmt)
    # Check if the status of the match = "Upcoming"
    if match.winner == "Upcoming":
        # Add the tip to the session.
        db.session.add(tip)
        # Commit the session.
        db.session.commit()
        # Return the tip to the user.
        return tip_schema.dump(tip)
    # If status does not = "Upcoming", return an error message. 
    else:
        return {"error": "Cannot make a selection on this match"}, 401

# Route to delete a tip.
@tips_bp.route("/<int:tip_id>", methods=["DELETE"])
# Check for a valid JWT.
@jwt_required()
def delete_tip(tip_id):
    # Fetch the tip from the database where the tip_id corresponds.
    stmt = db.select(Tip).filter_by(id=tip_id)
    tip = db.session.scalar(stmt)
    # If tip exists. 
    if tip:
        # Translate user id from tip to a string and compare to id from JWT
        if str(tip.user_id) != get_jwt_identity():
            # Return an error if user from JWT does not match user id
            return {"error": "You did not make this selection"}, 403
        # Delete the tip from the session.
        db.session.delete(tip)
        # Commit the session.
        db.session.commit()
        # Return a success message.
        return {"message": f"Tip deleted"}
    # If tip does not exist return an error message. 
    else:
        return {"error": f"Tip with id '{tip_id}' does not exist"}, 404
    
# Route to update a tip.
@tips_bp.route("/<int:tip_id>", methods=["PUT", "PATCH"])
# Check for a valid JWT. 
@jwt_required()
def update_tip(tip_id):
    # Fetch the data from the body of the request.
    body_data = tip_schema.load(request.get_json())
    #  Select the tip where tip_id corresponds from the request
    stmt = db.select(Tip).filter_by(id=tip_id)
    tip = db.session.scalar(stmt)
    # If the tip exists
    if tip:
        # If the string type of the tips user id does not equal the id from the JWT, return an error message.
        if str(tip.user_id) != get_jwt_identity():
            return {"error": "You did not make this selection"}, 403
        
        # Update the tip fields from the body of the request. 
        tip.selection = body_data.get("selection") or tip.selection
        tip.user_id = get_jwt_identity()
        tip.match_id = body_data.get("match_id") or tip.match_id
       # Select the match from the id in the body of the request. 
        match_stmt = db.select(Match).filter_by(id=body_data.get("match_id"))
        match = db.session.scalar(match_stmt)
        # Check the status of "winner" field in match and if it equls "Upcoming", commit the session
        if match.winner == "Upcoming":
            db.session.commit()
            # return the updated tip. 
            return tip_schema.dump(tip)
        # If the user does not match JWT identity return an error message. 
        else:
            return {"error": "You cannot update selection on this match"}
    # If the tip does not exist, return an error message. 
    else:
        return {"error": f"The tip with id '{tip_id} does  not exist"}, 404
    
# @tips_bp.route("/", methods=["DELETE"])
# @jwt_required()
# def delete_all_tips():
#     current_user = get_jwt_identity
#     stmt = db.select(Tip).filter_by(tips.user_id==current_user)
#     tips = db.session.scalars(stmt)
    
#     if not tips:
#         {"error": "No tips belonging to user"}

#     else:
#         db.session.delete(tips)
#         db.session.commit()
#         return {"message": f"All tips belonging to user id '{tips.users_id} have been deleted"}
    
        
