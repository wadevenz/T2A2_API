from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.location import Location, location_schema, locations_schema

location_bp = Blueprint("locations", __name__, url_prefix="/locations")

@location_bp.route("/")
@jwt_required()
def get_all_locations():
    stmt = db.select(Location)
    locations = db.session.scalars(stmt)
    return locations_schema.dump(locations)


