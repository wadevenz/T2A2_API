from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.team import Team, team_schema, teams_schema
from utils import auth_as_admin_decorator

teams_bp = Blueprint ("teams", __name__, url_prefix="/teams")

@teams_bp.route("/")
def get_all_teams():
    stmt = db.select(Team)
    teams = db.session.scalars(stmt)
    return teams_schema.dump(teams)

@teams_bp.route("/<int:teams_id>")
def get_team(teams_id):
    stmt = db.select(Team).filter_by(id=teams_id)
    team = db.session.scalar(stmt)
    
    if team:
        return team_schema.dump(team)
    else:
        return {"error": f"Team with id '{teams_id}' does not exist"}, 404
    
@teams_bp.route("/", methods=["POST"])
@jwt_required()
@auth_as_admin_decorator
def create_team():
    body_data = team_schema.load(request.get_json())
    
    team = Team(
            name=body_data.get("name"),
            stadium=body_data.get("stadium")
        )

    db.session.add(team)
    db.session.commit()

    return team_schema.dump(team)
    

@teams_bp.route("/<int:teams_id>", methods=["PUT", "PATCH"])
@jwt_required()
@auth_as_admin_decorator
def update_team(teams_id):
    body_data = team_schema.load(request.get_json())
    stmt = db.select(Team).filter_by(id=teams_id)
    team = db.session.scalar(stmt)

    if team:

        team.name = body_data.get("name") or team.name
        team.stadium = body_data.get("stadium") or team.stadium

        db.session.commit()

        return team_schema.dump(team)
    
    else:
        return {"error": f"Team with id '{teams_id}' does not exist"}
    

@teams_bp.route("/<int:teams_id>", methods=["DELETE"])
@jwt_required()
@auth_as_admin_decorator
def delete_team(teams_id):
    stmt = db.select(Team).filter_by(id=teams_id)
    team = db.session.scalar(stmt)

    if team:
        db.session.delete(team)
        db.session.commit()
        return {"message": f"Team with id '{teams_id}' has been deleted"}
    
    else:
        return {"error": f"Team with id '{teams_id}' does not exist"}, 404