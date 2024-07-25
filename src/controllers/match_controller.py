from datetime import datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.match import Match, match_schema, matches_schema
from utils import authorise_as_admin, auth_as_admin_decorator

match_bp = Blueprint("matches", __name__, url_prefix="/matches")

# Create endpoint to get all matches from the database.
@match_bp.route("/")
def get_all_matches():
    # Fetches all matches from database.
    stmt = db.select(Match)
    matches = db.session.scalars(stmt)
    # Utilise schema with many=true to return retrieved matches.
    return matches_schema.dump(matches)

# Endpoint to retrieve specific match.
@match_bp.route("/<int:match_id>")
def get_match(match_id):
    # Fetch match from database where match id matches route.
    stmt = db.select(Match).filter_by(id=match_id)
    match = db.session.scalar(stmt)
    # If the match exists, return the match.
    if match:
        return match_schema.dump(match)
    # If the match does not exist return an error message.
    else:
        return {"error": f"Match with id {match_id} not found"}
    
# Route to create a match on the database.
@match_bp.route("/", methods=["POST"])
# Requires a valid token from logged in user.
@jwt_required()
# Check to see if user is admin.
@auth_as_admin_decorator
def create_match():
    # Retrieves the JSON data from the body of the request.
    body_data = match_schema.load(request.get_json())
    # seperate instance of time value from the body of the request.
    time_data = body_data.get("time")
    # Check to see whether the time data is string datatype.
    if isinstance(time_data, str):
        try:
            # Creates object from the time data in the datetime format given.
            time = datetime.strptime(time_data, "%Y-%m-%d %H:%M")
        except ValueError:
            # If time data is a string but in the wrong format, return an error.
            return {"error": "Input format must be 'YYYY-MM-DD HH:MM'"}
        # Check if data from body is in datetime data type format.
    elif isinstance(time_data, datetime):
        # Creates the time object with body data. 
        time = time_data
    
    else:
        # If JSON body for time not a string or datetime type, return an error. 
        return {"error": "Input must be in the correct format, either string or datetime"}
    
    # Create an instance of match utilising JSON data from the body of the request.
    match = Match(
        round=body_data.get("round"),
        time=time,
        winner=body_data.get("winner"),
        location_id=body_data.get("location_id"),
        home_team_id=body_data.get("home_team_id"),
        away_team_id=body_data.get("away_team_id")
    )
    # Add instance to the session.
    db.session.add(match)
    # Commit the session.
    db.session.commit()
    # Return created match to user.
    return match_schema.dump(match)

# Route for updating a match.
@match_bp.route ("/<int:match_id>", methods=["PATCH", "PUT"])
# Check for a valid JWT.
@jwt_required()
# Check to see if user is an admin.
@auth_as_admin_decorator
def update_match(match_id):
    # Fetch the JSON data from the body of the request.
    body_data=match_schema.load(request.get_json(), partial=True)
    # Select the match that corresponds to the match id in the route.
    stmt = db.select(Match).filter_by(id=match_id)
    match= db.session.scalar(stmt)

    # If the match exists, update fields with body data or maintain original value.
    if match:
        match.round=body_data.get("round") or match.round
        match.time=body_data.get("time") or match.time
        match.winner=body_data.get("winner") or match.winner
        match.location_id=body_data.get("location_id") or match.location_id
        match.home_team_id=body_data.get("home_team_id") or match.home_team_id
        match.away_team_id=body_data.get("away_team_id") or match.away_team_id

        # Commit the changes.
        db.session.commit()
        # Return the updated match to the user
        return match_schema.dump(match)
    
    else:
        # Return an error if match does not exist. 
        return {"error": f"Match with id '{match_id}' does not exist"}, 404

# Route to delete a match
@match_bp.route("/<int:match_id>", methods=["DELETE"])
# Check for a valid JWT.
@jwt_required()
# Check that the user is an admin.
@auth_as_admin_decorator
def delete_match(match_id):
    # Fetch the match from the database with corresponding match id.
    stmt = db.select(Match).filter_by(id=match_id)
    match = db.session.scalar(stmt)
    # Check if match exists
    if match:
        # Delete the match.
        db.session.delete(match)
        # Commit the session.
        db.session.commit()
        # Return a message to the user.
        return {"message": f"Match with id '{match_id}' has been deleted"}
    # If match deos not exist, return an error message. 
    else:
        return {"error": f"Match with id '{match_id}' does not exist"}, 404



