# from flask import Blueprint, request
# from flask_jwt_extended import jwt_required, get_jwt_identity

# from init import db
# from models.tip import Tip, tip_schema, tips_schema

# tips_bp = Blueprint("tips", __name__, url_prefix="/tips")

# @tips_bp.route("/")
# def get_all_tips():
#     stmt = db.select(Tip)
#     tips = db.session.scalars(stmt)
#     return tips_schema.dump(tips)

# @tips_bp.route("/<int:tip_id>")
# def get_one_tip(tip_id):
#     stmt = db.select(Tip).filter_by(id=tip_id)
#     tip = db.session.scalar(stmt)
#     if tip:
#         return tip_schema.dump(tip)
#     else:
#         return {"error": f"Could not locate tip with id {tip_id}"}, 404

# @tips_bp.route("/<int:tip_id", methods=["POST"])
# @jwt_required()
# def create_tip():
#     pass