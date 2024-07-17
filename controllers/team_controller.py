from flask import Blueprint, request

from init import db
from models.team import Team, team_schema, teams_schema

teams_bp = Blueprint ("teams", __name__, url_prefix="/teams")

@teams_bp.route("/")
def get_all_teams():
    stmt = db.select(Team)
    teams = db.session.scalars(stmt)
    return teams_schema.dump(teams)