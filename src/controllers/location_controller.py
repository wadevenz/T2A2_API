from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.location import Location, location_schema, locations_schema
from utils import auth_as_admin_decorator

location_bp = Blueprint("locations", __name__, url_prefix="/locations")

# 
@location_bp.route("/")
def get_all_locations():
    stmt = db.select(Location)
    locations = db.session.scalars(stmt)
    return locations_schema.dump(locations)

@location_bp.route("/<int:locations_id>")
def get_location(locations_id):
    stmt = db.select(Location).filter_by(id=locations_id)
    location = db.session.scalar(stmt)

    if location:
        return location_schema.dump(location)
    
    else:
        return {"error": f"Location with id, {locations_id} does not exist"}, 404
    

@location_bp.route("/", methods=["POST"])
@jwt_required()
@auth_as_admin_decorator
def create_location():
    body_data = request.get_json()

    location = Location(
        city=body_data.get("city"),
        stadium=body_data.get("stadium"),
        timezone=body_data.get("timezone")
    )
    
    db.session.add(location)
    db.session.commit()

    return location_schema.dump(location)

@location_bp.route("/<int:locations_id>", methods=["DELETE"])
@jwt_required()
@auth_as_admin_decorator
def delete_location(locations_id):
    stmt = db.select(Location).filter_by(id=locations_id)
    location = db.session.scalar(stmt)

    if location:
        db.session.delete(location)
        db.session.commit()
        return {"message": f"Location with id '{locations_id}' has been deleted"}
    else:
        return {"error": f"Location with id '{locations_id}' does not exist"}, 404
    

@location_bp.route("/<int:locations_id>", methods=["PUT", "PATCH"])
@jwt_required()
@auth_as_admin_decorator
def update_location(locations_id):
    body_data = request.get_json()
    stmt = db.select(Location).filter_by(id=locations_id)
    location = db.session.scalar(stmt)

    if location:

        location.city=body_data.get("city") or location.city
        location.stadium=body_data.get("stadium") or location.stadium
        location.timezone=body_data.get("timezone") or location.timezone

        db.session.commit()

        return location_schema.dump(location)
    
    else:
        return {"error": f"Location with id '{locations_id}' does not exist"}, 404