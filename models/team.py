from marshmallow import fields

from init import db, ma

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    stadium = db.Column(db.String)

    matches = db.relationship('Match', back_populates="teams")

class TeamSchema(ma.Schema):
    matches = fields.Nested('MatchSchema', exclude=["teams"])

    class Meta:
        fields = ("id", "name", "stadium", "matches")

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)