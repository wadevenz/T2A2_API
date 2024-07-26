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

### Flask

Flask is a Python web applcation Framework that can be used to design API's, hence used in this project. Its popularity stems from its simplicity, versatility and self capability, meaning it has no external requirements and therefore works as an effective framework for this project written in the Python language. 

Python Software Foundation, 2024, PyPi, Flask 3.0.3, https://pypi.org/project/Flask/

### SQLAlchemy

As this application is utilising a relational database management system, PostgreSQL, the Object Relational Mapper and Python toolkit of SQLalchemy allows the relationship structure and schemas of the database to be mapped effectively on to the objects written in Python.

SQLAlchemy, viewed Jul 2024, https://www.sqlalchemy.org/

### Psycopg2

Using the Python language, the most common connection to the PostgreSQL database is via the database adapter of psycopg2. Its versatile and secure and works efficienty to match Python data types to PostgreSQL types. 

Python Software Foundation, 2024, pscopg2 2.9.9, https://pypi.org/project/psycopg2/

### Bcrypt

Bcrypt is a function that utilises cryptographics to hash a password, and then stores it in a back end for the purpose of significantly increasing password protection and data safety. 

Python Software Foundation, 2024, bcrypt 4.2.0, https://pypi.org/project/bcrypt/

### Marshmallow

Marshmallow is the 'middle-man' Python library, that enables the serialistaion and deserialisation of JSON data in our Flask application. It allows the JSON data types requested and sent from the front end to be read and validated, and manipulated into desired structures or schemas within the application.

Bharathwaj N, 2023, Marshmallow with Python Flask,https://medium.com/@nithinbharathwaj/marshmallow-with-python-flask-263e1fd5911f

### JWT Manager

Authorisation for interaction with data in this application is achieve using the common JSON Web Tokens. To do this more effectively the Javascript library JWT Mangager was installed.

### dotenv

The python-dotenv package allows the program to read key-value pair variables from ```.env``` files. This has been used to store sensive data contained with the URI and a secret JWT key. 

Python Software Foundation, 2024, python-dotenv 1.0.1, https://pypi.org/project/python-dotenv/

### Time/Date/Timezone libraries

A few modules and libraries have been installed to be able to access the databases and implement certain time and date variables within the application. 

## R4 Explain the benefits and drawbacks of this app’s underlying database system.

### PostgreSQL

PostgreSQL was the database system used for this application. It is an open source program that operates as an object-relational database management system. As this applications data suits an object structure of tables with columns that maintains relationships with other entities, the feature rich PostgreSQL fulfils the applications requirements well. Below is a brief outline of the database systems advantages and disadvantages. 

#### Benefits
**Object orientation** - As just mentioned, data stored in table structures with defined attributes and the ability to define comlex data types is a benefit, especially if designing a suitable application. Also within these data relationships is an inheritance structure which is important in object orientation (Ellingwood, 2024). 

**ACID compliance** - ACID refers to standards that are aimed to achieve maximum data validity and integrity when interacting with a database (Elligwood,2024). Its an acronym that can be explained through the folowing values:
 - **Atomicity** - Refers to indvisible transactions that maintain the function of all operations within that transaction. A transaction should and will not be finalised incomplete. 
 - **Consistency** - If data transitions through states, then the data integrity will be complete and maintained as it was pre transition. 
 - **Isolation** - Refers to data integrity being maintained through interactions as if every transaction was executed in sequential order.
 - **Durability** - Maintains all completed transactions through database failure or error. 
 
(Timescale, 2024)

**Conforms to SQL standards** - Compared to other similar systems, its increased adherence to SQL standards improves implementation of SQL functionality (Ellingwood, 2024)

**Open Source** - PostgreSQL is a popular open source project, which gives the benefit of a range of contrbutions to the development process (Ellingwood, 2024). Howver as seen below, open source may have some disadvantages. 

#### Drawbacks

**Open Source** - This can be a negative due to numerous owners rather than a single driving coorporate entity. Its broad input may have lead to poorer initial distribution and may also need higher clarity to maintain user friendliness. Also unlike other open source competitors PostgreSQL is not supported by as many market platforms and can suffer from compatability issues with some users(Ambarder, 2024). 

**Poor efficiency** - Compared to its closest competitor, the execution of concurrent dependencies can lead to decreased performance, especially if comparing to MySQL (Ambarder, 2024).

Ellingwood J, The benefits of PostgreSQL, viewed 2024 https://www.prisma.io/dataguide/postgresql/benefits-of-postgresql

Timescale, 2024, Understanding PostgreSQL, https://www.timescale.com/learn/understanding-postgresql

Dhruv S, 2024, PostgreSQL Advantages and Disadvantages, https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/

Ambarder S, 2024, What is PostgreSQL?, https://intellipaat.com/blog/what-is-postgresql/

## R5 Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

### SQLALChemy

**ORM purpose**

As this application utilises OOP or Object Oriented Programming, a bridge is required from the code of the application to the structure and schema of the database. We need software to act as a layer in between the two to help communicate and create the desired goal, this software is referred to as Object Relational Mapping. As discussed, our database management system is PostgreSQL, and our application is built within a Python framework. A popular and functional ORM for this purpose is SQLAlchemy. Discussed below are some key features and an example of its functionality within the application (Ellingwood, 2024).

**Features**

Function-based query construction - A significant feature, especially for this application is to allow functions, objects or expressions in Python language to construct SQL queries, which is important for simple and efficient implementation. 

Seperate mapping and class design - Like other ORMs it allows classes defined by a user to be mapped inline with table data utilising a "'Decalrative' configurational system" (SQLAlchemy,2024). Uniquely however it isolates this functionality into seperate implementations through the use of function.

Other features of SQLAlchemy include representing primary and foreign keys as sets of columns and also including composite primary keys. As well as a mature architecture and self referential object mapping, there is the ability for single and joined table inheritance. SQLAlchemy supports the retrieval of multiple inherited types from a single query
(SQLAlchemy, 2024)

**Functionality**

An important functional tool in this application is in mapping models for the database. 
An example of how this mapping is utilised in this app can be seen in the use of classes and subclasses in creating tables with attributes as columns in the database.

```db = SQLAlchemy()```
```def create_app():
    app = Flask(__name__)

    db.init_app(app)
```
First of all the app is created via a "Declarative Base" class and SQLAlchemy is instantiated to be utilised to create the example model with the table named "teams" as seen below.
```
class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
```
This subclass Team can also be given attributes states as a column as seen above. 

SQLAlchemy is also used within the app to show relationships between Models using primary and foreign keys. Below shows an example from the Tip model, showing a many to one relationship with the Match model.

```tips = db.relationship("Tip", back_populates="matches")```

Using the tool of SQLAlchemy effectively allows the appropriate translation from the framework of our app to the design and structure of the database in the end to allow us to make effective routes or endpoints to retrieve the data from the front end. 


SQLAlchemy, 2024, Features and Philosophy, https://www.sqlalchemy.org/features.html

Ellingwood J, 2024, What is an ORM? https://www.prisma.io/dataguide/types/relational/what-is-an-orm#:~:text=In%20general%2C%20ORMs%20serve%20as,from%20your%20language%20of%20choice.

## R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

![ERD](/docs/T2A2_ERD.png)


## R7 Explain the implemented models and their relationships, including how the relationships aid the database implementation.This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

### User Model

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

### Match Model

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

### Tip Model

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

### Team Model

```
class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    stadium = db.Column(db.String)

    matches = relationship('Match', primaryjoin="or_(Team.id==Match.home_team_id, Team.id==Match.away_team_id)", viewonly=True)
```

## R8 Explain how to use this application’s API endpoints. 

Comments within the applications code adhere to PEP 8 style guidelines. The comments will give a brief description in the controller about the functionality of each route and when error messages may occur. 

van Rossum W, Warsaw B, Coghlan A, 2013, PEP 8 – Style Guide for Python Code, https://peps.python.org/pep-0008/#comments

## **Auth & User**

### **HTTP Method** - POST

This endpoint is designed to register a new user. 

**Route or Path** - http://localhost:8080/auth/register

**Body Required**

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
This has returned a new registered user. As can be seen it displays the 'id' as a serial integer, and also displays the default setting for ```is_admin`` which is 'false'.

### **HTTP Method** - POST

This endpoint is designed to login a registered user. 

**Route or Path** - http://localhost:8080/auth/login

**Body Required**

name: The matching string value for this object stored in the database

email: The matching string value for this object stored in the database

password: The matching string value for this object stored in the database

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
This has returned a successful login from the user 'admin'. Unlike the above registered user, the result for ```is_admin``` is 'true', and it has also returned a JWT. This JWT is valid for 24hrs and authorises users for specific endpoints below. As this particular token belongs to an admin, authorisation is much broader as will be seen below. 

### **HTTP Method** - GET

This endpoint is designed to retrieve all users information. Authorised for admin only.

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
]
```
This has returned all users currently registered in the database. 

### **HTTP Method** - DELETE

Deletes a user. Must give valid JWT, therefore a user may only use this endpoint to delete themselves when logged in. 

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
Returns a message that the user has been deleted. 

### **HTTP Method** - PUT, PATCH 

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
Returns all the user fields with the updated fields displaying any new values.

## **Match**

### **HTTP Method** - GET

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
### **HTTP Method** - GET

Retrieves a single match from the database.

**Route or Path** - http://localhost:8080/matches/<int:match_id>

**Response**

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
This is returned match where the match_id = 1

### **HTTP Method** - POST

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
	"id": 10,
	"round": "21",
	"time": "2024-08-02 19:15",
	"locations": {
		"city": "Melbourne, Victoria",
		"stadium": "Marvel Stadium",
		"timezone": "Australia/Melbourne"
	},
	"home_team": {
		"name": "Western Bulldogs"
	},
	"away_team": {
		"name": "Melbourne Demons"
	},
	"winner": "Upcoming"
}
```

### **HTTP Method** - PUT, PATCH

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

### **HTTP Method** - DELETE

Deletes a match based on the id in the route. 

**Route or Path** - http://localhost:8080/matches/<int:match_id>

**Header Required**

token: A JWT from a logged in admin

**Response**

```
{
	"message": "Match with id '10' has been deleted"
}
```
This is an example return if endpoint was to delete match with id 10.

## **Tips**

### **HTTP Method** - GET

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

### **HTTP Method** - GET

Retrieves a single tip from the database. 

**Route or Path** - http://localhost:8080/tips/<int:tip_id>

**Header Required** 

token: A valid JWT is required from a user login. 

**Response** 
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
An example return from tip_id = 1

### **HTTP Method** - POST

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
A return of the created tip. Importantly tips can only be created or updated if the match in which a selection is being made has a "winner" value of "Upcoming" only, or an error will be sent. 

### **HTTP Method** - PUT, PATCH

Endpoint to update a specific tip. 

**Route or Path** - http://localhost:8080/tips/<int:tip_id>

**Body Required** - (Optional fields for the PATCH method)

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
### **HTTP Method** - DELETE

Delete a users tip from an authorised login

**Route or Path** - http://localhost:8080/tips/<int:tip_id>

**Header Required**

token: A valid JWT from the user corresponding to targeted tip. 

**Response**
```
{
	"message": "Tip deleted"
}
```
## **Location**

### **HTTP Method** - GET

Retrieve all teams from the database. 

**Route or Path** - http://localhost:8080/locations

**Response**
```
[
	{
		"id": 1,
		"city": "Brisbane, Queensland",
		"stadium": "Gabba",
		"timezone": "Australia/Queensland"
	},
	{
		"id": 2,
		"city": "Gold Coast, Queensland",
		"stadium": "People First Stadium",
		"timezone": "Australia/Queensland"
	},
	{
		"id": 3,
		"city": "Mount Barker, South Australia",
		"stadium": "Adelaide Hills",
		"timezone": "Australia/South"
	},
	{
		"id": 4,
		"city": "Adelaide, South Australia",
		"stadium": "Adelaide Oval",
		"timezone": "Australia/South"
	},
	{
		"id": 5,
		"city": "Hobart, Tasmaina",
		"stadium": "Blundstone Arena",
		"timezone": "Australia/Tasmania"
	},
	{
		"id": 6,
		"city": "Sydney, New South Wales",
		"stadium": "ENGIE Stadium",
		"timezone": "Australia/Sydney"
	},
	{
		"id": 7,
		"city": "Geelong, Victoria",
		"stadium": "GMHBA Stadium",
		"timezone": "Australia/Melbourne"
	},
	{
		"id": 8,
		"city": "Canberra, Australian Capital Territory",
		"stadium": "Manuka Oval",
		"timezone": "Australia/Sydney"
	},
	{
		"id": 9,
		"city": "Ballarat, Victoria",
		"stadium": "Mars Stadium",
		"timezone": "Australia/Victoria"
	},
	{
		"id": 10,
		"city": "Melbourne, Victoria",
		"stadium": "Marvel Stadium",
		"timezone": "Australia/Melbourne"
	},
	{
		"id": 11,
		"city": "Melbourne, Victoria",
		"stadium": "MCG",
		"timezone": "Australia/Melbourne"
	},
	{
		"id": 12,
		"city": "Norwood, South Australia",
		"stadium": "Norwood Oval",
		"timezone": "Australia/South"
	},
	{
		"id": 13,
		"city": "Perth, Australia",
		"stadium": "Optus Stadium",
		"timezone": "Australia/Perth"
	},
	{
		"id": 14,
		"city": "Sydney, New South Wales",
		"stadium": "SCG",
		"timezone": "Australia/Sydney"
	},
	{
		"id": 15,
		"city": "Darwin, Northern Territory",
		"stadium": "TIO Stadium",
		"timezone": "Australia/North"
	},
	{
		"id": 16,
		"city": "Alice Springs, Northern Territory",
		"stadium": "TIO Traeger Park",
		"timezone": "Australia/North"
	},
	{
		"id": 17,
		"city": "Launceston, Tasmania",
		"stadium": "UTAS Stadium",
		"timezone": "Australia/Tasmania"
	}
]
```
### **HTTP Method** - GET

Retrieve a single team from the database. 

**Route or Path** - http://localhost:8080/locations/<int:location_id>

**Response**
```
{
	"id": 4,
	"city": "Adelaide, South Australia",
	"stadium": "Adelaide Oval",
	"timezone": "Australia/South"
}
```
Example return where the location_id = 4

### **HTTP Method** - POST

Create a new location.

**Route or Path** - http://localhost:8080/locations

**Body Required**

city: A string identifying the city.

stadium: A string to identify the stadium. 

timezone: A string format to identify timezone. 

Example:
```
{
	"city": "Hobart, Tasmania",
	"stadium": "Macquarie Point Stadium",
	"timezone": "Australia/Tasmania"
}
```

**Header Required**

token: A valid token from an authorised admin user. 

**Response**
```
{
	"id": 18,
	"city": "Hobart, Tasmania",
	"stadium": "Macquarie Point Stadium",
	"timezone": "Australia/Tasmania"
}
```


### **HTTP Method** - PUT, PATCH 

Update an existing location

**Route or Path** - http://localhost:8080/locations/<int:location_id>

**Body Required** - (Optional fields for PATCH method)

city: A string identifying the city.

stadium: A string to identify the stadium. 

timezone: A string format to identify timezone. 

Example:
```
{
	"city": "Hobart, Tasmania",
	"stadium": "Bellrive Oval",
	"timezone": "Australia/Tasmania"
}
```

**Header Required**

token: A valid token from an authorised admin user. 

**Response**
```
{
	"id": 18,
	"city": "Hobart, Tasmania",
	"stadium": "Bellrive Oval",
	"timezone": "Australia/Tasmania"
}
```

### **HTTP Method** - DELETE

Delete an existing location from the database. 

**Route or Path** - http://localhost:8080/locations/<int:location_id>

**Header Required**

token: A valid JWT that is associated with an authorised admin. 

**Response**
```
{
	"message": "Location with id '18' has been deleted"
}
```
Example: location_id = 18

## **Teams**

### **HTTP Method** - GET

Retrieve all teams from the database. 

**Route or Path** - http://localhost:8080/teams

**Response**
```
[
	{
		"id": 1,
		"name": "Brisbane Lions",
		"stadium": "Gabba"
	},
	{
		"id": 2,
		"name": "Gold Coast Suns",
		"stadium": "People First Stadium"
	},
	{
		"id": 3,
		"name": "Sydney Swans",
		"stadium": "SCG"
	},
	{
		"id": 4,
		"name": "GWS Giants",
		"stadium": "Engie Stadium, Manuka Oval"
	},
	{
		"id": 5,
		"name": "Carlton Blues",
		"stadium": "Marvel Stadium"
	},
	{
		"id": 6,
		"name": "Geelong Cats",
		"stadium": "GMHBA Stadium"
	},
	{
		"id": 7,
		"name": "Fremantle Dockers",
		"stadium": "Optus Stadium"
	},
	{
		"id": 8,
		"name": "Essendon Bombers",
		"stadium": "Marvel Stadium"
	},
	{
		"id": 9,
		"name": "Melbourne Demons",
		"stadium": "MCG"
	},
	{
		"id": 10,
		"name": "Port Adelaide Power",
		"stadium": "Adelaide Oval"
	},
	{
		"id": 11,
		"name": "Western Bulldogs",
		"stadium": "Marvel Stadium, Mars Stadium"
	},
	{
		"id": 12,
		"name": "Hawthorn Hawks",
		"stadium": "MCG, UTAS Stadium"
	},
	{
		"id": 13,
		"name": "Adelaide Crows",
		"stadium": "Adelaide Oval"
	},
	{
		"id": 14,
		"name": "Collingwood Magpies",
		"stadium": "MCG"
	},
	{
		"id": 15,
		"name": "St Kilda",
		"stadium": "Marvel Stadium"
	},
	{
		"id": 16,
		"name": "West Coast Eagles",
		"stadium": "Optus Stadium"
	},
	{
		"id": 17,
		"name": "North Melbourne Kangaroos",
		"stadium": "Marvel Stadium, Blundstone Arena"
	},
	{
		"id": 18,
		"name": "Richmond Tigers",
		"stadium": "MCG"
	}
]
```

### **HTTP Method** - GET

Retrieve a single team from the database. 

**Route or Path** - http://localhost:8080/teams/<int:team_id>

**Response**
```
{
	"id": 1,
	"name": "Brisbane Lions",
	"stadium": "Gabba"
}
```
Example: team_id = 1

### **HTTP Method** - POST

Create a new team. 

**Route or Path** - http://localhost:8080/teams

**Body Required** 

name: A String with a character limit of 100

stadium: A String to identify the appropriate stadium. 

Example: 
```
{
	"name": "Tasmanian Devils",
	"stadium": "Macquarie Point"
}
```

**Header Required** 

token: A valid JWT associated with an authorised admin user. 

**Response**
```
{
	"id": 19,
	"name": "Tasmanian Devils",
	"stadium": "Macquarie Point"
}
```
### **HTTP Method** - PUT, PATCH

This endpoint is designed to update a team. 

**Route or Path** - http://localhost:8080/teams/<int:team_id>

**Body Required** 

name: A String with a character limit of 100

stadium: A String to identify the appropriate stadium. 

Example: 
```
{
	"name": "Tasmanian Devils",
	"stadium": "Bellrive Ovalt"
}
```

**Header Required** 

token: A valid JWT associated with an authorised admin user. 

**Response**
```
{
	"id": 19,
	"name": "Tasmanian Devils",
	"stadium": "Bellrive Ovalt"
}
```
### **HTTP Method**- DELETE

Deletes a team from the database. 

**Route or Path** - http://localhost:8080/teams/<int:team_id>

**Header Required**

token: A valid JWT from an authorised admin. 

**Response**
```
{
	"message": "Team with id '19' has been deleted"
}
```
Example: team_id = 19
