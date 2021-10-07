"""CRUD operations."""

from model import db, User, Favorite, Animal, Breed, Animal_type, connect_to_db


def create_user(email, password,first_name, last_name, phone_number):
    """Create and return a new user."""

    user = User(email=email, password=password, fname= first_name, lname= last_name, phone_number = phone_number)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)



def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_animals(animal_id, animal_name, animal_description, fixed, receive_date, available_date, age, gender, weight, breed_id, animal_type_id):
    """Create and return a new animal."""

    animal = Animal(
        animal_id=animal_id,
        animal_name=animal_name,
        animal_description=animal_description,
        fixed=fixed,
        receive_date=receive_date,
        available_date=available_date,
        age=age,
        gender=gender,
        weight=weight,
        breed_id=breed_id,
        animal_type_id=animal_type_id
    )

    db.session.add(animal)
    db.session.commit()

    return animal


def get_animals():
    """Return all animals."""

    return Animal.query.all()


def get_animal_by_id(animal_id):
    """Return a animal by primary key."""

    return Animal.query.get(animal_id)


def create_favorite(favorite_id, animal_id, user_id):
    """Create and return a new favorite."""


    favorite = Favorite(favorite_id=favorite_id, animal_id=animal_id, user_id=user_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite




def get_favorite_by_id(favorite_id):
    """Return a favorite by primary key."""

    return Favorite.query.get(favorite_id)


def create_animal_type(animal_type_id, animal_type):
    """Create and return a new animal_type."""

    animal_type = Animal_type(animal_type_id=animal_type_id, animal_type=animal_type)

    db.session.add(animal_type)
    db.session.commit()

    return animal_type

def get_animal_type_by_id(animal_type_id):
    """Return a animal type by primary key."""

    return Animal_type.query.get(animal_type_id)

def create_breed(breed_id, breed):
    """Create and return a new breed."""

    breed = Breed(breed_id=breed_id, breed=breed)

    db.session.add(breed)
    db.session.commit()

    return breed


def get_breed_by_id(breed_id):
    """Return a breed by primary key."""

    return Breed.query.get(breed_id)



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
