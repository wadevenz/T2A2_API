
from marshmallow import fields
from marshmallow.validate import OneOf

from init import db, ma


VALID_WINNER = ("Home", "Away", "Draw", "Upcoming", "Live")

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String)
    time = db.Column(db.DateTime)
    winner = db.Column(db.String)
    
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)

    locations = db.relationship("Location", back_populates="matches")
    home_team = db.relationship("Team", foreign_keys=[home_team_id])
    away_team = db.relationship("Team", foreign_keys=[away_team_id])
    
    tips = db.relationship("Tip", back_populates="matches")

class MatchSchema(ma.Schema):

    locations = fields.Nested('LocationSchema', exclude=["id"])
    home_team = fields.Nested('TeamSchema', only=["name"])
    away_team = fields.Nested('TeamSchema', only=["name"])

    home_team_id = fields.Integer(load_only=True)
    away_team_id = fields.Integer(load_only=True)
    location_id = fields.Integer(load_only=True)

    winner = fields.String(required=True, validate=OneOf(VALID_WINNER), error="Winner must contain a valid input")

    time = fields.DateTime(format='%Y-%m-%d %H:%M', required=True)

    class Meta:
        fields = ("id", "round", "time", "locations", "home_team", "away_team", "winner", "location_id", "home_team_id", "away_team_id")
        ordered = True

match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)