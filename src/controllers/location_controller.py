from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.location import Location, location_schema, locations_schema
from utils import auth_as_admin_decorator

location_bp = Blueprint("locations", __name__, url_prefix="/locations")

# Route to retrieve all locations from the database
@location_bp.route("/")
def get_all_locations():
    # Fetch all locations from the database
    stmt = db.select(Location)
    locations = db.session.scalars(stmt)
    # Return locations to user. 
    return locations_schema.dump(locations)

# Route to retrieve single location
@location_bp.route("/<int:locations_id>")
def get_location(locations_id):
    # Fetch single location from database filtering by location id
    stmt = db.select(Location).filter_by(id=locations_id)
    location = db.session.scalar(stmt)
    # If location exists return location to user. 
    if location:
        return location_schema.dump(location)
    # If no location exists return an error message. 
    else:
        return {"error": f"Location with id, {locations_id} does not exist"}, 404
    
# Route to create a location.
@location_bp.route("/", methods=["POST"])
# Check for a valid token
@jwt_required()
# Check to see if the user is an admin. 
@auth_as_admin_decorator
def create_location():
    # Retrieve JSON data from the body of the request
    body_data = request.get_json()
    # Create a location instance utilisng the body data. 
    location = Location(
        city=body_data.get("city"),
        stadium=body_data.get("stadium"),
        timezone=body_data.get("timezone")
    )
    # Add the location to the session.
    db.session.add(location)
    # Commit the session.
    db.session.commit()
    # Return the location to the user. 
    return location_schema.dump(location)

# Route to delete a location
@location_bp.route("/<int:locations_id>", methods=["DELETE"])
# Check for a valid token
@jwt_required()
# Check if the user is an admin
@auth_as_admin_decorator
def delete_location(locations_id):
    # Fetch the location filtering by id
    stmt = db.select(Location).filter_by(id=locations_id)
    location = db.session.scalar(stmt)
    # If the location exists
    if location:
        # Delete the location
        db.session.delete(location)
        # Commit the session and retrun message. 
        db.session.commit()
        return {"message": f"Location with id '{locations_id}' has been deleted"}
    #If the location does not exist, return an error message.
    else:
        return {"error": f"Location with id '{locations_id}' does not exist"}, 404
    
# Route to update a location
@location_bp.route("/<int:locations_id>", methods=["PUT", "PATCH"])
# Check for a valid token.
@jwt_required()
# Check to see if the user is an admin. 
@auth_as_admin_decorator
def update_location(locations_id):
    # Retrieve the JSON data from the body of the request. 
    body_data = request.get_json()
    # Fetch the location filtering by location id
    stmt = db.select(Location).filter_by(id=locations_id)
    location = db.session.scalar(stmt)
    # If the location exists
    if location:
        # Update the fields using the body data or maintain original values. 
        location.city=body_data.get("city") or location.city
        location.stadium=body_data.get("stadium") or location.stadium
        location.timezone=body_data.get("timezone") or location.timezone
        # Commit the session
        db.session.commit()
        # Return the location to the user. 
        return location_schema.dump(location)
    # If the location does not exist, return an error message. 
    else:
        return {"error": f"Location with id '{locations_id}' does not exist"}, 404