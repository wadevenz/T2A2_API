# Wade Venz T2A2

## AFL Tips API

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

### R1 Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

On its face, creating a footy tipping API might appear that it tackles no significant purpose or goal. Instead, it seems to exist merely to make available basic AFL information allow the amusement of friends and colleagues for some light hearted fun and hard but friendly competition through tipping... and that is true. 

However, there is much to be said for the benefits of an easy-to-use, enjoyable tipping competition, especially in a safe and friendly environment where no money is exchanged. It enhances engagement with sport, encouraging even the most casual of fans to follow matches closely and discuss predictions with friends and colleagues. 

It fosters camaraderie and friendly competition among participants, leading to social interaction and bonding over shared interests. In a workplace, or community setting, it also enhances morale by bringing colleagues together over a shared activity.

I have utilised such applications in the past, and I have enjoyed the friendly competition it creates, as it enhances the thrill of the match and creates lively conversations amongst pals. And it appears I'm not alone, as Barrett disccusses that a friendly tipping competition can engage inclusivity and foster communication in the workplace (Barrett, 2018).

Therefore the simple objectiove of this API application is to give AFL fans access to a live database of basic AFL information, including teams, locations, matches and give the option to make selections on the team they believe will win in upcoming matches. Simple in theory, effective in practice. Users have limited ability to manipulate data in the database as most requests are for admin authorisation only. This simplifies the application to give users access to information and the ability to make and update selections. And yet while it may seem that without reward or fincancial incentive, the selection process appears redundant, the reward is the enhanced thrill of following your chosen selection and the competitve incentive to beat your fellow associates. 

Barrett, S, 2018, Is footy tipping the missing link for a great company culture?, viewed Jul, 2024, https://www.linkedin.com/pulse/footy-tipping-missing-link-great-company-culture-scott-barrett/

### R2 Describe the way tasks are allocated and tracked in your project.

[Trello](https://trello.com/b/vHCD0owm/t2a2api)


### R3 List and explain the third-party services, packages and dependencies used in this app.

### R4 Explain the benefits and drawbacks of this app’s underlying database system.

### R5 Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

### R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

### R7 Explain the implemented models and their relationships, including how the relationships aid the database implementation.This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

### R8 Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:  - HTTP verb  - Path or route  - Any required body or header data  - Response