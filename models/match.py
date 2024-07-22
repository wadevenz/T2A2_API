
from marshmallow import fields, validates
from marshmallow.validate import OneOf

from init import db, ma


VALID_WINNER = ("Home", "Away", "Draw", "Upcoming", "Live")

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String)
    time = db.Column(db.Date)
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

    winner = fields.String(required=True, validate=OneOf(VALID_WINNER), error="Winner must contain a valid input")

    # @validates("winner")
    # def validate_status(self, value):
    #    pass
            
    class Meta:
        fields = ("id", "round", "time", "winner", "locations", "home_team", "away_team")
        ordered = True

match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)