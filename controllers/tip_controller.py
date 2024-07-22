from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.tip import Tip, tip_schema, tips_schema
from models.match import Match

tips_bp = Blueprint("tips", __name__, url_prefix="/tips")

@tips_bp.route("/")
def get_all_tips():
    stmt = db.select(Tip)
    tips = db.session.scalars(stmt)
    return tips_schema.dump(tips)

@tips_bp.route("/<int:tip_id>")
def get_one_tip(tip_id):
    stmt = db.select(Tip).filter_by(id=tip_id)
    tip = db.session.scalar(stmt)
    if tip:
        return tip_schema.dump(tip)
    else:
        return {"error": f"Could not locate tip with id {tip_id}"}, 404

@tips_bp.route("/", methods=["POST"])
@jwt_required()
def create_tip():
    body_data = request.get_json()
    
    tip = Tip(
        selection=body_data.get("selection"),
        user_id=get_jwt_identity(),
        match_id=body_data.get("match_id")
    )

    stmt = db.select(Match).filter_by(id=body_data.get("match_id"))
    match = db.session.scalar(stmt)

    if match.winner == "Upcoming":
        db.session.add(tip)
        db.session.commit()
        return tip_schema.dump(tip)
    
    else:
        return {"error": "Cannot make a selection on this match"}, 401

@tips_bp.route("/<int:tip_id>", methods=["DELETE"])
@jwt_required()
def delete_tip(tip_id):
    stmt = db.select(Tip).filter_by(id=tip_id)
    tip = db.session.scalar(stmt)

    if tip:
        db.session.delete(tip)
        db.session.commit()
        return {"message": f"Tip deleted"}
    else:
        return {"error": f"Tip with id '{tip_id}' does not exist"}, 404
    
# @tips_bp.route("/", methods=["DELETE"])
# @jwt_required()
# def delete_all_tips():
#     stmt = db.select(Tip)
#     tips = db.session.scalars(stmt)
#     db.session.delete(tips)
#     db.session.commit()
#     return {"message": "All tips deleted"}


@tips_bp.route("/<int:tip_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_tip(tip_id):
    body_data = request.get_json()
    stmt = db.select(Tip).filter_by(id=tip_id)
    tip = db.session.scalar(stmt)
    if tip:
        
        if str(tip.user_id) != get_jwt_identity():
            return {"error": "You did not make this tip"}, 403
        
        tip.selection = body_data.get("selection") or tip.selection
        tip.user_id = get_jwt_identity()
        tip.match_id = body_data.get("match_id") or tip.match_id
       
        match_stmt = db.select(Match).filter_by(id=body_data.get("match_id"))
        match = db.session.scalar(match_stmt)

        if match.winner == "Upcoming":
            db.session.commit()
        
            return tip_schema.dump(tip)
        else:
            return {"error": "You cannot update selection on this match"}
    
    else:
        return {"error": f"The tip with id '{tip_id} does  not exist"}, 404