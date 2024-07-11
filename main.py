import os

from flask import Flask

from init import db, ma, bcrypt, jwt

# Application Factory (setup the app within a function)

def create_app():
    app = Flask(__name__)

# utilised a os environement to protect sensitive info in .env file
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

# initialised the dependencies 

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app

