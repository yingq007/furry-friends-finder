"""Models for furry friends finder app."""

from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()


class User(db.Model):
    """Data Model for a user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100))

    animals = db.relationship("Animal", secondary="favorites", backref="users")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Favorite(db.Model):
    "Data Model for favorite"

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.animal_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return f'<Favorite favorite_id={self.favorite_id} animal_id={self.animal_id} user_id ={self.user_id}>'


class Animal(db.Model):
    "Data Model for animal"

    __tablename__ = "animals"

    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_name = db.Column(db.String(25))
    animal_description = db. Column(db.String, unique=True)
    spayed_neutered = db.Column(db.String)
    age = db.Column(db.String)
    gender = db. Column(db.String)
    primary_breed = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)
    url = db.Column(db.String)
    photo = db.Column(db.String)
    organization_animal_id = db.Column(db.String)



    def __repr__(self): 
        return f'<Animal animal_id={self.animal_id} animal_name={self.animal_name} animal_description={self.animal_description} spayed_neutered={self.spayed_neutered} age={self.age} gender={self.gender} primary_breed={self.primary_breed} email={self.email} phone_number={self.phone_number} url={self.url} photo={self.photo} organization_animal_id={self.organization_animal_id}>'


def connect_to_db(flask_app, db_uri="postgresql:///furry_friends_finder", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    import os
    

    os.system("dropdb furry_friends_finder --if-exists")
    os.system("createdb furry_friends_finder")

    connect_to_db(app)

    db.create_all()