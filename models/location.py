
from init import db, ma

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    stadium = db.Column(db.String)
    timezone = db.Column(db.Date)

class LocationSchema(ma.Schema):
    class Meta:
        fields = ("id", "city", "stadium", "timezone")

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)