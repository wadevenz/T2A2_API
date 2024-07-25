from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.team import Team, team_schema, teams_schema
from utils import auth_as_admin_decorator

teams_bp = Blueprint ("teams", __name__, url_prefix="/teams")
# Route to retrieve all teams.
@teams_bp.route("/")
def get_all_teams():
    # Fetch all teams from the database. 
    stmt = db.select(Team)
    teams = db.session.scalars(stmt)
    # Return the teams to the user. 
    return teams_schema.dump(teams)

# Route to retrieve a single team
@teams_bp.route("/<int:teams_id>")
def get_team(teams_id):
    # Fetch a single team from the database filtering by id. 
    stmt = db.select(Team).filter_by(id=teams_id)
    team = db.session.scalar(stmt)
    # If the team exists, return the team to the user. 
    if team:
        return team_schema.dump(team)
    # If the team does not exist, return an error message. 
    else:
        return {"error": f"Team with id '{teams_id}' does not exist"}, 404

# Route to create a new team. 
@teams_bp.route("/", methods=["POST"])
# Check for a vail token. 
@jwt_required()
# Check if the user is an admin. 
@auth_as_admin_decorator
def create_team():
    # Retrieve the JSON data from the body of the request. 
    body_data = team_schema.load(request.get_json())
    
    # Create a new instance of team using the body data. 
    team = Team(
            name=body_data.get("name"),
            stadium=body_data.get("stadium")
        )
    # Add the team to the session.
    db.session.add(team)
    # Commit the session.
    db.session.commit()
    # Return the team to the user. 
    return team_schema.dump(team)
    
# Route to update existing team. 
@teams_bp.route("/<int:teams_id>", methods=["PUT", "PATCH"])
# Check for a valid token 
@jwt_required()
# Check if the user is an admin. 
@auth_as_admin_decorator
def update_team(teams_id):
    # Retrieve the JSON data from the body of the request. 
    body_data = team_schema.load(request.get_json())
    # Fetch the team filtering by id. 
    stmt = db.select(Team).filter_by(id=teams_id)
    team = db.session.scalar(stmt)
    # If the team exists update fields using body data or maintaining existing values. 
    if team:

        team.name = body_data.get("name") or team.name
        team.stadium = body_data.get("stadium") or team.stadium
        # Commit the session. 
        db.session.commit()
        # Return the team to the user. 
        return team_schema.dump(team)
    # If the team does not exist, return an error message.
    else:
        return {"error": f"Team with id '{teams_id}' does not exist"}
    
# Route to delete a single team.
@teams_bp.route("/<int:teams_id>", methods=["DELETE"])
# Check for a valid token. 
@jwt_required()
# Check if the user is an admin. 
@auth_as_admin_decorator
def delete_team(teams_id):
    # Fetch the team filtering by id.
    stmt = db.select(Team).filter_by(id=teams_id)
    team = db.session.scalar(stmt)
    # If the team exists, delete the team, commit the session and return a message. 
    if team:
        db.session.delete(team)
        db.session.commit()
        return {"message": f"Team with id '{teams_id}' has been deleted"}
    # If team does not exist, return an error message. 
    else:
        return {"error": f"Team with id '{teams_id}' does not exist"}, 404