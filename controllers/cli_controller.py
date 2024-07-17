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
            name="Brisbane Lions",
            stadium="Gabba"
        ),
         Team(
            name="Gold Coast Suns",
            stadium="People First Stadium"
        ),
         Team(
            name="Sydney Swans",
            stadium="SCG"
        ),
         Team(
            name="GWS Giants",
            stadium="Engie Stadium, Manuka Oval"
        ),
         Team(
            name="Carlton Blues",
            stadium="Marvel Stadium"
        ),
         Team(
            name="Geelong Cats",
            stadium="GMHBA Stadium"
        ),
         Team(
            name="Fremantle Dockers",
            stadium="Optus Stadium"
        ),
         Team(
            name="Essendon Bombers",
            stadium="Marvel Stadium"
        ),
         Team(
            name="Melbourne Demons",
            stadium="MCG"
        ),
         Team(
            name="Port Adelaide Power",
            stadium="Adelaide Oval"
        ),
         Team(
            name="Western Bulldogs",
            stadium="Marvel Stadium, Mars Stadium"
        ),
         Team(
            name="Hawthorn Hawks",
            stadium="MCG, UTAS Stadium"
        ),
         Team(
            name="Adelaide Crows",
            stadium="Adelaide Oval"
        ),
         Team(
            name="Collingwood Magpies",
            stadium="MCG"
        ),
         Team(
            name="St Kilda",
            stadium="Marvel Stadium"
        ),
         Team(
            name="West Coast Eagles",
            stadium="Optus Stadium"
        ),
         Team(
            name="North Melbourne Kangaroos",
            stadium="Marvel Stadium, Blundstone Arena"
        ),
         Team(
            name="Richmond Tigers",
            stadium="MCG"
        )
    ]

    db.session.add_all(teams)


    db.session.commit()

    print("Tables seeded")