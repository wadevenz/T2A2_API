
from marshmallow import fields, validates
from marshmallow.validate import OneOf

from init import db, ma


# VALID_WINNER = ("Home", "Away", "Draw", "Upcoming")

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String)
    time = db.Column(db.Date)
    winner = db.Column(db.String)
    
    location_id = db.Column(db.String, db.ForeignKey("location.id", nullable=False))
    home_team = db.Column(db.String, db.ForeignKey("teams.id"), nullable=False)
    away_team = db.Column(db.String, db.ForeignKey("teams.id"), nullable=False)

    locations = db.relationship("Location", back_populates="matches")

class MatchSchema(ma.Schema):

    locations = fields.Nested('LocationSchema', only=["stadium"])

    # winner = fields.String(validate=OneOf(VALID_WINNER))

    # @validates("winner")
    # def validate_status(self, value):
    #    pass
            
    class Meta:
        fields = ("id", "round", "time", "winner", "locations", "home_team", "away_team")


match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)