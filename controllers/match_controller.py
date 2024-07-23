from datetime import datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.match import Match, match_schema, matches_schema

match_bp = Blueprint("matches", __name__, url_prefix="/matches")

@match_bp.route("/")
@jwt_required()
def get_all_matches():
    stmt = db.select(Match)
    matches = db.session.scalars(stmt)
    return matches_schema.dump(matches)

@match_bp.route("/<int:match_id>")
@jwt_required()
def get_match(match_id):
    stmt = db.select(Match).filter_by(id=match_id)
    match = db.session.scalar(stmt)
    
    if match:
        return match_schema.dump(match)
    else:
        return {"error": f"Match with id {match_id} not found"}
    

@match_bp.route("/", methods=["POST"])
@jwt_required()
def create_match():
    body_data = match_schema.load(request.get_json())
    
    match = Match(
        round=body_data.get("round"),
        time=body_data.get("time"),
        winner=body_data.get("winner"),
        location_id=body_data.get("location_id"),
        home_team_id=body_data.get("home_team_id"),
        away_team_id=body_data.get("away_team_id")
    )
    
    db.session.add(match)
    db.session.commit()
    
    return match_schema.dump(match)

@match_bp.route ("/<int:match_id>", methods=["PATCH", "PUT"])
@jwt_required()
def update_match(match_id):
    body_data=match_schema.load(request.get_json(), partial=True)
    stmt = db.select(Match).filter_by(id=match_id)
    match= db.session.scalar(stmt)

    if match:
        match.round=body_data.get("round") or match.round
        match.time=body_data.get("time") or match.time
        match.winner=body_data.get("winner") or match.winner
        match.location_id=body_data.get("location_id") or match.location_id
        match.home_team_id=body_data.get("home_team_id") or match.home_team_id
        match.away_team_id=body_data.get("away_team_id") or match.away_team_id

        db.session.commit()

        return match_schema.dump(match)
    
    else:
        return {"error": f"Match with id '{match_id}' does not exist"}, 404


@match_bp.route("/<int:match_id>", methods=["DELETE"])
@jwt_required()
def delete_card(match_id):
    stmt = db.select(Match).filter_by(id=match_id)
    match = db.session.scalar(stmt)
    if match:
        db.session.delete(match)
        db.session.commit()
        return {"message": f"Match with id '{match_id}' has been deleted"}
    else:
        return {"error": f"Match with id '{match_id}' does not exist"}, 404
