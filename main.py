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

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)
    
    from controllers.team_controller import teams_bp
    app.register_blueprint(teams_bp)
    
    from controllers.tip_controller import tips_bp
    app.register_blueprint(tips_bp)

    return app

