"""Models for furry friends finder app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Data Model for a user"""
    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(25), nullable=False, unique=True)
    fname = db.Column(db.String(25), nullable=False, unique=True)
    lname = db.Column(db.String(25), nullable=False, unique=True) 
    email = db.Column(db.String(100),nullable=False, unique=True)
    phone_number = db.Column(db.String(25), nullable=False, unique=True) 

    animals = db.relationship('Animal', back_populates = 'User')


    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Favorite(db.Model):
    "Data Model for favorite"
    __tablename__ = "Favorites"
    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('Animals.animal_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))

    User = db.relationship('Favorites', back_populates =  'User')
    Animal = db.relationship('Favorite', back_populates = 'Animal')

class Animal(db.Model):
    """Data model for an animal."""
    __tablename__ = "Animals"
    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'))
    name = db.Column(db.String(50), nullable=False, unique=True)
    animal_species = db.Column(db.String(25), nullable=False, unique=True)
    birth_year = db.Column(db.Integer, nullable=False)

    human = db.relationship('Human', back_populates="animals")

    def __repr__(self):
        return f"<animal id={self.animal_id} name={self.name} species={self.animal_species}>"

class Rating(db.Model):
    """A movie rating."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
