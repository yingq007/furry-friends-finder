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
    spayed_neutered = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    gender = db. Column(db.String)
    breed = db.Column(db.String)

    # breed = db.relationship('Breed', backref = 'animals')
    # animal_type = db.relationship('Animal_type', backref = 'animals')

    def __repr__(self): 
        return f'<Animal animal_id={self.animal_id} animal_name={self.animal_name}>'


# class Breed(db.Model):
#     "Data Model for breed"

#     __tablename__ = "breeds"

#     breed_id = db.Column(db.Integer, primary_key=True)
#     breed = db.Column(db.String(25))

#     # animals = db.relationship('Animal', backref = "breeds")

#     def __repr__(self): 
#         return f'<Breed breed_id={self.breed_id} breed={self.breed}>'


# class Animal_type(db.Model):
#     "Data Model for animal type"

#     __tablename__ = "animal_types"

#     animal_type_id = db.Column(db.Integer, primary_key= True)
#     animal_type = db.Column(db.String(25))

#     # animals = db.relationship('Animal', backref= "animal_types")

#     def __repr__(self): 
#         return f'<Animal_type animal_type_id={self.animal_type_id}>'


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