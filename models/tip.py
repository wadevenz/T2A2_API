from init import db, ma

from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError

VALID_SELECTION = ( "Home", "Away", "Draw" )

class Tip(db.Model):
    __tablename__ = "tips"

    id = db.Column(db.Integer, primary_key=True)
    selection = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users"), nullable=False)
    # match_id = db.Column(db.Integer, db.ForeignKey("matches", nullable=False))

    user = db.relationship ('User', back_populates = "tips")
    # match = db.relationship ('Match', back_populates = "tips")

class TipSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ["name", "email"] )
    # match = fields.List(fields.Nested('MatchSchema', only = ["id", "round", "time", "home_team", "away_team", "winner"]))

    selection = fields.String(validate=OneOf(VALID_SELECTION))
    
    class Meta:
        fields = ("id", "selection", "user")

tip_schema = TipSchema()
tips_schema = TipSchema(many=True)