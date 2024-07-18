from init import db, ma

from marshmallow import fields

class Tip(db.Model):
    __tablename__ = "tips"

    id = db.Column(db.Integer, primary_key=True)
    selection = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users"), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("matches", nullable=False))

    user = db.relationship ('User', back_populates = "tips")
    matches = db.relationship ('Match', back_populates = "tips")

class TipSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ["name", "email"] )
    matches = fields.List(fields.Nested('MatchSchema', only = ["round", "winner"]))

    class Meta:
        fields = ("id", "selection", "user", "matches")

tip_schema = TipSchema()
tips_schema = TipSchema(many=True)