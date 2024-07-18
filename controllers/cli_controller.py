from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.team import Team
from models.location import Location
from models.match import Match


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

    matches =[
        Match(
            round="20",
            time=datetime(2024, 7, 26, 19, 40),
            winner="Upcoming",
            location=locations[9],
            home_team=teams[4],
            away_team=teams[9]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 27, 13, 45),
            winner="Upcoming",
            location=locations[4],
            home_team=teams[16],
            away_team=teams[5]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 27, 16, 35),
            winner="Upcoming",
            location=locations[1],
            home_team=teams[1],
            away_team=teams[0]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 27, 16, 35),
            winner="Upcoming",
            location=locations[9],
            home_team=teams[14],
            away_team=teams[7]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 27, 19, 30),
            winner="Upcoming",
            location=locations[10],
            home_team=teams[8],
            away_team=teams[3]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 27, 20, 10),
            winner="Upcoming",
            location=locations[12],
            home_team=teams[6],
            away_team=teams[15]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 28, 13, 10),
            winner="Upcoming",
            location=locations[10],
            home_team=teams[13],
            away_team=teams[17]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 28, 15, 20),
            winner="Upcoming",
            location=locations[13],
            home_team=teams[2],
            away_team=teams[10]
        ),
        Match(
            round="20",
            time=datetime(2024, 7, 28, 16, 10),
            winner="Upcoming",
            location=locations[3],
            home_team=teams[12],
            away_team=teams[11]
        ),
    ]
    db.session.add_all(matches)

    db.session.commit()

    print("Tables seeded")