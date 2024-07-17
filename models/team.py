from init import db, ma

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    stadium = db.Column(db.String)

class TeamSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "stadium")

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)