from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.team import Team


db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            name="admin",
            email="admin@email.com",
            password=bcrypt.generate_password_hash("password123").decode("utf-8"),
            is_admin=True
        ),
        User(
            name="guest",
            email="guest@email.com",
            password=bcrypt.generate_password_hash("password123").decode("utf-8")
        )
    ]
    db.session.add_all(users)

    teams = [
        Team(
            name="Brisbane Lions"
        ),
         Team(
            name="Gold Coast Suns"
        ),
         Team(
            name="Sydney Swans"
        ),
         Team(
            name="GWS Giants"
        ),
         Team(
            name="Carlton Blues"
        ),
         Team(
            name="Geelong Cats"
        ),
         Team(
            name="Fremantle Dockers"
        ),
         Team(
            name="Essendon Bombers"
        ),
         Team(
            name="Melbourne Demons"
        ),
         Team(
            name="Port Adelaide Power"
        ),
         Team(
            name="Western Bulldogs"
        ),
         Team(
            name="Hawthorn Hawks"
        ),
         Team(
            name="Adelaide Crows"
        ),
         Team(
            name="Collingwood Magpies"
        ),
         Team(
            name="St Kilda"
        ),
         Team(
            name="West Coast Eagles"
        ),
         Team(
            name="North Melbourne Kangaroos"
        ),
         Team(
            name="Richmond Tigers"
        )
    ]

    db.session.add_all(teams)


    db.session.commit()

    print("Tables seeded")