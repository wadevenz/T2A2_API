from marshmallow import fields, validates

from init import db, ma


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    stadium = db.Column(db.String)
    timezone = db.Column(db.Date)

    matches = db.relationship("Match", back_populates="locations")

class LocationSchema(ma.Schema):

    matches = fields.List(fields.Nested('MatchSchema', only=["round", "time", "winner"]))

    class Meta:
        fields = ("id", "city", "stadium", "timezone", "matches")

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)