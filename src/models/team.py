from marshmallow import fields
from sqlalchemy.orm import relationship

from init import db, ma


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    stadium = db.Column(db.String)

    matches = relationship('Match', primaryjoin="or_(Team.id==Match.home_team_id, Team.id==Match.away_team_id)", viewonly=True)
class TeamSchema(ma.Schema):

    matches = fields.List(fields.Nested('MatchSchema', exclude=["teams"]))

    class Meta:
        fields = ("id", "name", "stadium")
        ordered = True

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)