import os

from flask import Flask

from init import db, ma, bcrypt, jwt

# Application Factory (setup the app within a function)

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://olympic_dev:123456@localhost:5432/olympics_db"

    app.config["JWT_SECRET_KEY"] = "secret"

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app

