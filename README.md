# AFL Tips API

## Wade Venz T2A2

### Initial setup
[Github](https://github.com/wadevenz/T2A2_API)

 - Clone the repo to your machine

 - Open 'src' folder and create and activate virtual environment
     - ```python3 -m venv .venv```
     - ```source .venv/bin/activate```

- Install dependencies
    - ```pip3 install -r requirements.txt```

- In PostgreSQL, create a database and role to interact with API
    - ```CREATE DATABASE t2a2_db;```
    - ``` CREATE ROLE assessment_dev && GRANT ALL ON t2a2_db TO assessment_dev;```

- Create file .env to reflect .env.sample and add values, for example:
    - ```DATABASE_URL="postgresql+psycopg2://assessment_dev:123456@localhost:5432/t2a2_db"```

    - ```JWT_SECRET_KEY= "confidential"```

- Create and seed the database
    - ```flask db create```
    - ```flask db seed```

- Start the server
    - ```flask run```

Please note: To remove the application from development debug mode, enter .flaskenv file and replace 'FLASK_DEBUG=1' to 'FLASK_DEBUG=0'.

Comments within the applications code adhere to PEP 8 style guidelines.
van Rossum W, Warsaw B, Coghlan A, 2013, PEP 8 – Style Guide for Python Code, https://peps.python.org/pep-0008/#comments

## R1 Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

On its face, creating a footy tipping API might appear that it tackles no significant purpose or goal. Instead, it seems to exist merely to make available basic AFL information allow the amusement of friends and colleagues for some light hearted fun and hard but friendly competition through tipping... and that is true. 

However, there is much to be said for the benefits of an easy-to-use, enjoyable tipping competition, especially in a safe and friendly environment where no money is exchanged. It enhances engagement with sport, encouraging even the most casual of fans to follow matches closely and discuss predictions with friends and colleagues. 

It fosters camaraderie and friendly competition among participants, leading to social interaction and bonding over shared interests. In a workplace, or community setting, it also enhances morale by bringing colleagues together over a shared activity.

I have utilised such applications in the past, and I have enjoyed the friendly competition it creates, as it enhances the thrill of the match and creates lively conversations amongst pals. And it appears I'm not alone, as Barrett disccusses that a friendly tipping competition can engage inclusivity and foster communication in the workplace (Barrett, 2018).

Therefore the simple objectiove of this API application is to give AFL fans access to a live database of basic AFL information, including teams, locations, matches and give the option to make selections on the team they believe will win in upcoming matches. Simple in theory, effective in practice. Users have limited ability to manipulate data in the database as most requests are for admin authorisation only. This simplifies the application to give users access to information and the ability to make and update selections. And yet while it may seem that without reward or fincancial incentive, the selection process appears redundant, the reward is the enhanced thrill of following your chosen selection and the competitve incentive to beat your fellow associates. 

Barrett, S, 2018, Is footy tipping the missing link for a great company culture?, viewed Jul, 2024, https://www.linkedin.com/pulse/footy-tipping-missing-link-great-company-culture-scott-barrett/

## R2 Describe the way tasks are allocated and tracked in your project.

[Trello](https://trello.com/b/vHCD0owm/t2a2api)

The planning and project allocation tool I used for this application was trello. The software provides templates with which gives a good indication of desirable workflow.

Tasks are split up into 5 cards; Brainstorm, Todo, Doing and Done. As this was a similar task to undertake as had been previously seen, most tasks were automatically assigned to the 'Todo' card at the beginning. However as this was a first time solo project of this nature, inevitably other tasks were assigned as they were presented along the timeline of the project.

If the task was large enough, sub tasks were added within them in the form of checklists. This enabled effective breakdown of tasks and also mitigated the risk of leaving some tasks undone. 

Significant tasks were also given target completion dates, which highlighted their importance and enabled better planning. 

![Trello](/docs/T2A2_Trello.png)

## R3 List and explain the third-party services, packages and dependencies used in this app.

#### Flask

Flask is a Python web applcation Framework that can be used to design API's, hence used in this project. Its popularity stems from its simplicity, versatility and self capability, meaning it has no external requirements and therefore works as an effective framework for this project written in the Python language. 

Python Software Foundation, 2024, PyPi, Flask 3.0.3, https://pypi.org/project/Flask/

#### SQLAlchemy

As this application is utilising a relational database management system, PostgreSQL, the Object Relational Mapper and Python toolkit of SQLalchemy allows the relationship structure and schemas of the database to be mapped on to the objects written in Python.

SQLAlchemy, viewed Jul 2024, https://www.sqlalchemy.org/

#### Psycopg2

Using the Python language, the most common connection to the PostgreSQL databse is via the database adapter of psycopg2. Its versatile and secure and works efficienty to mathc Python data types to PostgreSQL types. 

Python Software Foundation, 2024, pscopg2 2.9.9, https://pypi.org/project/psycopg2/

#### Bcrypt

Bcrypt is a function that utilises cryptographics to hash a password, and then stores it in a back end for the purpose of significantly increasing password protection and data safety. 

Python Software Foundation, 2024, bcrypt 4.2.0, https://pypi.org/project/bcrypt/

#### Marshmallow

Marshmallow is the 'middle-man' Python library, that enables the serialistaion and deserialisation of JSON data in our Flask application. It allows the JSON data types requested and sent from the front end to be read and validated, and manipulated into desired structures or schemas within the application.

Bharathwaj N, 2023, Marshmallow with Python Flask,https://medium.com/@nithinbharathwaj/marshmallow-with-python-flask-263e1fd5911f

#### JWT Manager

Authorisation for interaction with data in this application is mostly using the common JSON Web Tokens. To do this more effectively the Javascript library JWT Mangager was installed.

#### dotenv

The python-dotenv package allows the program to read ky-value pair variables from ```.env``` files. This has been used to store sensive data contained with the URI and a secret JWT key. 

Python Software Foundation, 2024, python-dotenv 1.0.1, https://pypi.org/project/python-dotenv/

#### Time/Date/Timezone libraries

A few modules and libraries have been installed to be able to access the databases and implement certain variables within the application. 

## R4 Explain the benefits and drawbacks of this app’s underlying database system.

#### PostgreSQL
##### Benefits

##### Drawbacks

## R5 Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

#### SQLALChemy

ORM purpose



Features
- Function-based query construction
- Seperate mapping and class design
- Mature high performing architecture
- Composite primary keys
- self-referential Object Mappings

Functionality

An important functional tool in this application is in mapping models for the database. 
An example of how this mapping is utilised in this app can be seen in the use of classes and subclasses in creating tables with attributes as columns in the database.

```db = SQLAlchemy()```
```def create_app():
    app = Flask(__name__)

    db.init_app(app)
```
First of all the app is created via a "Declarative Base" class and SQLAlchemy is instantiated to be utilised to create the example model below.
```
class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
```
The subclass Team can be defined as a Model and declare a tablename which reflects a table in the database. Attributes can then be added declared as a Column as seen above. 

SQLAlchemy is also used within the app to declare relationships between Models primary and foreign keys. Below shows an example from the Tip model, showing a many to one relationship with the Match model.

```tips = db.relationship("Tip", back_populates="matches")```

## R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

![ERD](/docs/T2A2_ERD.png)


## R7 Explain the implemented models and their relationships, including how the relationships aid the database implementation.This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

#### Match Model

```
class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.String)
    time = db.Column(db.DateTime)
    winner = db.Column(db.String)
    
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)

    locations = db.relationship("Location", back_populates="matches")
    home_team = db.relationship("Team", foreign_keys=[home_team_id])
    away_team = db.relationship("Team", foreign_keys=[away_team_id])
    
    tips = db.relationship("Tip", back_populates="matches")
```

#### Tip Model

```
class Tip(db.Model):
    __tablename__ = "tips"

    id = db.Column(db.Integer, primary_key=True)
    selection = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"), nullable=False)

    users = db.relationship ('User', back_populates = "tips")
    matches = db.relationship ('Match', back_populates = "tips")
```

#### Location Model

```
class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    stadium = db.Column(db.String)
    timezone = db.Column(db.String)

    matches = db.relationship("Match", back_populates="locations")
```

#### Team Model

```
class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    stadium = db.Column(db.String)

    matches = relationship('Match', primaryjoin="or_(Team.id==Match.home_team_id, Team.id==Match.away_team_id)", viewonly=True)
```

#### User Model

```
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    tips = db.relationship("Tip", back_populates="users")
```


## R8 Explain how to use this application’s API endpoints. 

### **Auth & User**

**HTTP Method** - POST

Registering a new user. 

**Route or Path** - http://localhost:8080/auth/register

**Body Required**

Default fields: id and a boolean value for is_admin

Required Fields: name, email, password

name: A string of maximum 100 characters
email: Must be in the format of "string"@"string"."string"
password: A string with a minimum of eight characters with at least one Integer and Alpha character. 

Example:
```
"name": "Dev 1",
"email": "dev1@email.com",
"password": "password123"
```
**Response**
```
{
	"id": 3,
	"name": "Dev 1",
	"email": "dev1@email.com",
	"is_admin": false
}
```

**HTTP Method** - POST

Login a user. 

**Route or Path** - http://localhost:8080/auth/login

**Body Required**

name: The matching string value stored in database

email: The matching string value stored in database

password: The matching string value stored in database

Example:
```
"name": "admin",
"email": "admin@email.com",
"password": "password123"
```
**Response**
```
{
	"name": "admin",
	"email": "admin@email.com",
	"is_admin": true,
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMTg4MTkwOCwianRpIjoiZDcyMzkxMWUtNzg4NS00YTA4LTliZWYtNjkwODQxZmM0MDAwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3MjE4ODE5MDgsImNzcmYiOiI1MGQzZTFhYi02YmE5LTRkMGQtODI5Zi0zZTVkNTNjZWQxYTciLCJleHAiOjE3MjE5NjgzMDh9.xMgSAY06__87jdpulgJVSdxcZoWjuVeTI2tzrMDjqMw"
}
```

**HTTP Method** - GET

Retrieve all users information. Authorised for admin only.

**Route or Path** - http://localhost:8080/auth/users

**Header Required**

token: The JWT from a logged in admin for authorisation:

**Response**
```
[
	{
		"id": 1,
		"name": "admin",
		"email": "admin@email.com",
		"is_admin": true
	},
	{
		"id": 2,
		"name": "guest",
		"email": "guest@email.com",
		"is_admin": false
	},
	{
		"id": 3,
		"name": "Dev 1",
		"email": "dev1@email.com",
		"is_admin": false
	},
	{
		"id": 5,
		"name": "Dev 2",
		"email": "dev2@email.com",
		"is_admin": false
	}
]
```

**HTTP Method** - DELETE

Deletes a user. Must give valid JWT, therefore a user may only delete themselves. 

**Route or Path** - http://localhost:8080/auth/users

**Header Required**

token: The JWT from a logged in user.

**Response**

Example: User from logged in user id "5"
```
{
	"message": "User with id '5' has been deleted"
}
```

**HTTP Method** - PUT, PATCH 

Updates a users details. The user must be logged in as a valid JWT is required. 

**Route or Path** - http://localhost:8080/auth/users

**Body Required** - (Optional fields in PATCH method)

name: The matching string value stored in database

email: The matching string value stored in database

password: The matching string value stored in database

```
{
	"name": "Developer 1",
	"email": "developer1@email.com",
	"password": "123password"
} 
```
**Header Required**

token: The JWT from the logged in user, in this example "Dev 1".

**Response**
```
{
	"id": 3,
	"name": "Developer 1",
	"email": "developer1@email.com",
	"is_admin": false
}
```

### **Match**

**HTTP Method** - GET

Retrieves all matches from the database.

**Route or Path** - http://localhost:8080/matches

**Response**
```
[
	{
		"id": 1,
		"round": "20",
		"time": "2024-07-26 19:40",
		"locations": {
			"city": "Melbourne, Victoria",
			"stadium": "Marvel Stadium",
			"timezone": "Australia/Melbourne"
		},
		"home_team": {
			"name": "Carlton Blues"
		},
		"away_team": {
			"name": "Port Adelaide Power"
		},
		"winner": "Upcoming"
	},
	{
		"id": 2,
		"round": "20",
		"time": "2024-07-27 13:45",
		"locations": {
			"city": "Hobart, Tasmaina",
			"stadium": "Blundstone Arena",
			"timezone": "Australia/Tasmania"
		},
		"home_team": {
			"name": "North Melbourne Kangaroos"
		},
		"away_team": {
			"name": "Geelong Cats"
		},
		"winner": "Upcoming"
	},
	{
		"id": 3,
		"round": "20",
		"time": "2024-07-27 16:35",
		"locations": {
			"city": "Gold Coast, Queensland",
			"stadium": "People First Stadium",
			"timezone": "Australia/Queensland"
		},
		"home_team": {
			"name": "Gold Coast Suns"
		},
		"away_team": {
			"name": "Brisbane Lions"
		},
		"winner": "Upcoming"
	},
	{
		"id": 4,
		"round": "20",
		"time": "2024-07-27 16:35",
		"locations": {
			"city": "Melbourne, Victoria",
			"stadium": "Marvel Stadium",
			"timezone": "Australia/Melbourne"
		},
		"home_team": {
			"name": "St Kilda"
		},
		"away_team": {
			"name": "Essendon Bombers"
		},
		"winner": "Upcoming"
	},
	{
		"id": 5,
		"round": "20",
		"time": "2024-07-27 19:30",
		"locations": {
			"city": "Melbourne, Victoria",
			"stadium": "MCG",
			"timezone": "Australia/Melbourne"
		},
		"home_team": {
			"name": "Melbourne Demons"
		},
		"away_team": {
			"name": "GWS Giants"
		},
		"winner": "Upcoming"
	},
	{
		"id": 6,
		"round": "20",
		"time": "2024-07-27 20:10",
		"locations": {
			"city": "Perth, Australia",
			"stadium": "Optus Stadium",
			"timezone": "Australia/Perth"
		},
		"home_team": {
			"name": "Fremantle Dockers"
		},
		"away_team": {
			"name": "West Coast Eagles"
		},
		"winner": "Upcoming"
	},
	{
		"id": 7,
		"round": "20",
		"time": "2024-07-28 13:10",
		"locations": {
			"city": "Melbourne, Victoria",
			"stadium": "MCG",
			"timezone": "Australia/Melbourne"
		},
		"home_team": {
			"name": "Collingwood Magpies"
		},
		"away_team": {
			"name": "Richmond Tigers"
		},
		"winner": "Upcoming"
	},
	{
		"id": 8,
		"round": "20",
		"time": "2024-07-28 15:20",
		"locations": {
			"city": "Sydney, New South Wales",
			"stadium": "SCG",
			"timezone": "Australia/Sydney"
		},
		"home_team": {
			"name": "Sydney Swans"
		},
		"away_team": {
			"name": "Western Bulldogs"
		},
		"winner": "Upcoming"
	},
	{
		"id": 9,
		"round": "20",
		"time": "2024-07-28 16:10",
		"locations": {
			"city": "Adelaide, South Australia",
			"stadium": "Adelaide Oval",
			"timezone": "Australia/South"
		},
		"home_team": {
			"name": "Adelaide Crows"
		},
		"away_team": {
			"name": "Hawthorn Hawks"
		},
		"winner": "Upcoming"
	}
]
```
**HTTP Method** - GET

Retrieves a match from the database.

**Route or Path** - http://localhost:8080/matches/<int:match_id>

**Response**

Example: match_id=1
```
{
	"id": 1,
	"round": "20",
	"time": "2024-07-26 19:40",
	"locations": {
		"city": "Melbourne, Victoria",
		"stadium": "Marvel Stadium",
		"timezone": "Australia/Melbourne"
	},
	"home_team": {
		"name": "Carlton Blues"
	},
	"away_team": {
		"name": "Port Adelaide Power"
	},
	"winner": "Upcoming"
}
```

**HTTP Method** - POST

Creates a match for the database. Admin only authorised for action.

**Route or Path** - http://localhost:8080/matches

**Body Required**

round: A string representing the round or week the match is being undertaken. e.g "10" or "Grand Final"

time: A string in the format of "YYYY-MM-DD HH:MM"

winner: Must be one of the following strings: "Home", "Away", "Draw", "Upcoming", "Live"

location_id: An integer corresponding to the id of a location in the database.

home_team_id: An integer corresponding to the id of a team in the database

away_team_id: An integer corresponding to the id of a team in the database

Example:
```
{
	"round": "21",
	"time": "2024-08-02 19:15",
	"winner": "Upcoming",
	"location_id": "10",
	"home_team_id": "11",
	"away_team_id": "9"
}
```

**Response**
```
{
	"round": "21",
	"time": "2024-08-02 19:15",
	"winner": "Upcoming",
	"location_id": "10",
	"home_team_id": "11",
	"away_team_id": "9"
}
```

**HTTP Method** - PUT, PATCH

Updates a particular match based on the match id in the route. 

**Route or Path** - http://localhost:8080/matches/<int:match_id>

**Body Required** - (Optional fields in PATCH method)

round: A string representing the round or week the match is being undertaken. e.g "10" or "Grand Final"

time: A string in the format of "YYYY-MM-DD HH:MM"

winner: Must be one of the following strings: "Home", "Away", "Draw", "Upcoming", "Live"

location_id: An integer corresponding to the id of a location in the database.

home_team_id: An integer corresponding to the id of a team in the database

away_team_id: An integer corresponding to the id of a team in the database

Example:
```
{
	"round": "21",
	"time": "2024-08-02 19:15",
	"winner": "Live",
	"location_id": "1",
	"home_team_id": "1",
	"away_team_id": "2"
}
```

**Header Required**

token: A JWT is required from a logged in admin. 

**Response**
```
{
	"id": 1,
	"round": "21",
	"time": "2024-08-02 19:15",
	"locations": {
		"city": "Brisbane, Queensland",
		"stadium": "Gabba",
		"timezone": "Australia/Queensland"
	},
	"home_team": {
		"name": "Brisbane Lions"
	},
	"away_team": {
		"name": "Gold Coast Suns"
	},
	"winner": "Live"
}
```

**HTTP Method** - DELETE

Deletes a match based on the id in the route. 

**Route or Path** - http://localhost:8080/matches/<int:match_id>

**Header Required**

token: A JWT from a logged in admin

**Response**

Example: match_id = 10
```
{
	"message": "Match with id '10' has been deleted"
}
```

### **Tips**

**HTTP Method** - GET

Retrieves all tips from the database. 

**Route or Path** - http://localhost:8080/tips

**Header Required** 

token: A valid JWT is required from a user login. 

**Response** 
```
[
	{
		"id": 1,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 1,
			"round": "21",
			"winner": "Live",
			"home_team": {
				"name": "Brisbane Lions"
			},
			"away_team": {
				"name": "Gold Coast Suns"
			}
		}
	},
	{
		"id": 2,
		"selection": "Away",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 2,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "North Melbourne Kangaroos"
			},
			"away_team": {
				"name": "Geelong Cats"
			}
		}
	},
	{
		"id": 3,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 3,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "Gold Coast Suns"
			},
			"away_team": {
				"name": "Brisbane Lions"
			}
		}
	},
	{
		"id": 4,
		"selection": "Away",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 4,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "St Kilda"
			},
			"away_team": {
				"name": "Essendon Bombers"
			}
		}
	},
	{
		"id": 5,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 5,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "Melbourne Demons"
			},
			"away_team": {
				"name": "GWS Giants"
			}
		}
	},
	{
		"id": 6,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 6,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "Fremantle Dockers"
			},
			"away_team": {
				"name": "West Coast Eagles"
			}
		}
	},
	{
		"id": 7,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 7,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "Collingwood Magpies"
			},
			"away_team": {
				"name": "Richmond Tigers"
			}
		}
	},
	{
		"id": 8,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 8,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "Sydney Swans"
			},
			"away_team": {
				"name": "Western Bulldogs"
			}
		}
	},
	{
		"id": 9,
		"selection": "Home",
		"users": {
			"name": "guest"
		},
		"matches": {
			"id": 9,
			"round": "20",
			"winner": "Upcoming",
			"home_team": {
				"name": "Adelaide Crows"
			},
			"away_team": {
				"name": "Hawthorn Hawks"
			}
		}
	}
]
```

**HTTP Method** - GET

Retrieves a single tip from the database. 

**Route or Path** - http://localhost:8080/tips/<int:tip_id>

**Header Required** 

token: A valid JWT is required from a user login. 

**Response** 

Example: tip_id = 1
```
{
	"id": 1,
	"selection": "Home",
	"users": {
		"name": "guest"
	},
	"matches": {
		"id": 1,
		"round": "21",
		"winner": "Live",
		"home_team": {
			"name": "Brisbane Lions"
		},
		"away_team": {
			"name": "Gold Coast Suns"
		}
	}
}
```

**HTTP Method** - POST

Endpoint to create a tip. 

**Route or Path** - http://localhost:8080/tips

**Body Required**

selection: One of a valid string selection; "Home" or "Away" 

user_id: An integer corresponding to the id of the user.

match_id: An integer corresponding to the id of the match. 

```
"selection": "Home",
"user_id": "1",
"match_id": "2"
```

**Header Required** 

token: A valid JWT from the logged in user. 

**Response**
```
{
	"id": 10,
	"selection": "Home",
	"users": {
		"name": "admin"
	},
	"matches": {
		"id": 2,
		"round": "20",
		"winner": "Upcoming",
		"home_team": {
			"name": "North Melbourne Kangaroos"
		},
		"away_team": {
			"name": "Geelong Cats"
		}
	}
}
```

**HTTP Method** - PUT, PATCH

Endpoint to update a specific tip. 

**Route or Path** - http://localhost:8080/tips/<int:tip_id>

**Body Required** - (OPtional fields for the PATCH method)

selection: One of a valid string selection; "Home" or "Away" 

user_id: An integer corresponding to the id of the user.

match_id: An integer corresponding to the id of the match. 

```
"selection": "Away",
"user_id": "1",
"match_id": "2"
```

**Header Required** 

token: A valid JWT from the logged in user. 

**Response**
```
{
	"id": 10,
	"selection": "Home",
	"users": {
		"name": "admin"
	},
	"matches": {
		"id": 2,
		"round": "20",
		"winner": "Upcoming",
		"home_team": {
			"name": "North Melbourne Kangaroos"
		},
		"away_team": {
			"name": "Geelong Cats"
		}
	}
}
```
**HTTP Method** - DELETE

Delete a users tip from an authorised login

**Route or Path** - http://localhost:8080/tips/<int:tip_id>

**Header Required**

token: A valid JWT from the user corresponding to targeted tip. 

**Response**

Example: tip_id = 10
```
{
	"message": "Tip deleted"
}
```

### **Location**

### **Teams**

