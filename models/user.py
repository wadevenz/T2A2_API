from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    tips = db.relationship("Tip", back_populates="users")

class UserSchema(ma.Schema):

    tips = fields.List(fields.Nested("TipSchema", exclude=["user"]))

    # email = fields.String(required=True, validate=Regexp("^\S+@\S+\.\S+$", error="Invalid Email Format"))

    # password = fields.String(required=True, validate=Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error="Minimum eight characters, at least one letter and one number"))


    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "tips")

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])



