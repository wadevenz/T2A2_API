# from flask import Blueprint, request

# from init import db
# from models.tip import Tip, tip_schema, tips_schema

# tips_bp = Blueprint("tips", __name__, url_prefix="/tips")

# @tips_bp.route("/")
# def get_all_tips():
#     stmt = db.select(Tip)
#     tips = db.session.scalars(stmt)
#     return tips_schema.dump(tips)

