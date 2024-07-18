from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.team import Team
from models.location import Location


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

    locations = [
        Location(
            city="Brisbane, Queensland",
            stadium="Gabba",
            # timezone=datetime(2024, tzinfo=ZoneInfo("Australia/Queensland"))
        ),
          Location(
            city="Gold Coast, Queensland",
            stadium="People First Stadium",
            # timezone=ZoneInfo("Australia/Queensland")
        ),
          Location(
            city="Mount Barker, South Australia",
            stadium="Adelaide Hills",
            # timezone=ZoneInfo("Australia/South")
        ),
          Location(
            city="Adelaide, South Australia",
            stadium="Adelaide Oval",
            # timezone=ZoneInfo("Australia/South")
        ),
          Location(
            city="Hobart, Tasmaina",
            stadium="Blundstone Arena",
            # timezone=ZoneInfo("Australia/Tasmania")
        ),
          Location(
            city="Sydney, New South Wales",
            stadium="ENGIE Stadium",
            # timezone=ZoneInfo("Australia/Sydney")
        ),
          Location(
            city="Geelong, Victoria",
            stadium="GMHBA Stadium",
            # timezone=ZoneInfo("Australia/Melbourne")
        ),
          Location(
            city="Canberra, Australian Capital Territory",
            stadium="Manuka Oval",
            # timezone=ZoneInfo("Australia/Sydney")
        ),
          Location(
            city="Ballarat, Victoria",
            stadium="Mars Stadium",
            # timezone=ZoneInfo("Australia/Victoria")
        ),
          Location(
            city="Melbourne, Victoria",
            stadium="Marvel Stadium",
            # timezone=ZoneInfo("Australia/Melbourne")
        ),
          Location(
            city="Melbourne, Victoria",
            stadium="MCG",
            # timezone=ZoneInfo("Australia/Melbourne")
        ),
          Location(
            city="Norwood, South Australia",
            stadium="Norwood Oval",
            # timezone=ZoneInfo("Australia/South")
        ),
          Location(
            city="Perth, Australia",
            stadium="Optus Stadium",
            # timezone=ZoneInfo("Australia/Perth")
        ),
          Location(
            city="Sydney, New South Wales",
            stadium="SCG",
            # timezone=ZoneInfo("Australia/Sydney")
        ),
          Location(
            city="Darwin, Northern Territory",
            stadium="TIO Stadium",
            # timezone=ZoneInfo("Australia/North")
        ),
          Location(
            city="Alice Springs, Northern Territory",
            stadium="TIO Traeger Park",
            # timezone=ZoneInfo("Australia/North")
        ),
          Location(
            city="Launceston, Tasmania",
            stadium="UTAS Stadium",
            # timezone=ZoneInfo("Australia/Tasmania")
        ),
    ]
    db.session.add_all(locations)

    db.session.commit()

    print("Tables seeded")