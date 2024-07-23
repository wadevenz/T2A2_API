import functools

from flask_jwt_extended import get_jwt_identity

from init import db
from models.user import User

def authorise_as_admin():
    try:
        users_id = get_jwt_identity()
        stmt = db.select(User).filter_by(id=users_id)
        user = db.session.scalar(stmt)

        return user.is_admin
    except AttributeError:
        return {"error": "User not found"}, 404
    
def auth_as_admin_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        users_id = get_jwt_identity()
        stmt = db.select(User).filter_by(id=users_id)
        user = db.session.scalar(stmt)
        if user.is_admin:
            return fn(*args, **kwargs)
        else:
            return {"error": "Only admin can perform this action"}, 403

    return wrapper

