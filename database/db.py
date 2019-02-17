from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class FootballTable(db.Model):
    __tablename__ = 'football'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    age = db.Column(db.INTEGER)

    def __init__(self, id, name, position, age):
        self.id = id
        self.name = name
        self.position = position
        self.age = age


class Football_schema(ma.Schema):
    class Meta():
        fields = ('id', 'name', 'position', 'age')


football_schema = Football_schema()
footballs_schema = Football_schema(many=True)


class UserTable(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, age, email, password):
        self.username = username
        self.age = age
        self.email = email
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'age', 'email', 'password')


user_schema = UserSchema()
