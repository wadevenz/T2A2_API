from init import db, ma

from marshmallow import fields, validates
from marshmallow.validate import OneOf

VALID_SELECTION = ("Home", "Away")

class Tip(db.Model):
    __tablename__ = "tips"

    id = db.Column(db.Integer, primary_key=True)
    selection = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"), nullable=False)

    users = db.relationship ('User', back_populates = "tips")
    matches = db.relationship ('Match', back_populates = "tips")

class TipSchema(ma.Schema):

    users = fields.Nested('UserSchema', only = ["name"] )
    matches = fields.Nested('MatchSchema', only = ["id", "round", "winner", "home_team", "away_team"])

    selection = fields.String(validate=OneOf(VALID_SELECTION))

    class Meta:
        fields = ("id", "selection", "users", "matches")
        ordered = True

tip_schema = TipSchema()
tips_schema = TipSchema(many=True)