from datetime import timedelta, datetime

from marshmallow import fields

from init import db, ma

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String, nullable=False)
    time = db.Column(db.Date)
    winner = db.Column(db.String)
    
    location_id = db.Column(db.String, db.ForeignKey("location.id", nullable=False))
    home_team = db.Column(db.String, db.ForeignKey("teams.id"), nullable=False)
    away_team = db.Column(db.String, db.ForeignKey("teams.id"), nullable=False)

    location = db.relationship('Location', back_populates = "match")

class MatchSchema():

    location = fields.Nested('LocationSchema')

    class Meta:
        fields = ("id", "round", "time", "winner", "location_id", "home_team", "away_team")


match_schema = MatchSchema()
matches_schema = MatchSchema(many=True)