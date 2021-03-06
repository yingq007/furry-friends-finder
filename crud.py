"""CRUD operations."""

from model import db, User, Favorite, Animal, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

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


def create_animal(animal_name, animal_description, spayed_neutered, age, gender, primary_breed, email, phone_number, url, photo, organization_animal_id):
    """Create and return a new animal."""

    animal = Animal(
        animal_name=animal_name,
        animal_description=animal_description,
        spayed_neutered=spayed_neutered,
        age=age,
        primary_breed=primary_breed,
        email=email,
        phone_number=phone_number,
        url=url,
        photo=photo,
        organization_animal_id=organization_animal_id
    )

    db.session.add(animal)
    db.session.commit()

    return animal




def get_animal_by_id(animal_id):
    """Return a animal by primary key."""

    return Animal.query.get(animal_id)


def create_favorite(animal_id, user_id):
    """Create and return a new favorite."""


    favorite = Favorite(animal_id=animal_id, user_id=user_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_favorite_by_id(favorite_id):
    """Return a favorite by primary key."""

    return Favorite.query.get(favorite_id)

def get_animal_by_animal_name_and_organization_animal_id(animal_name, organization_animal_id):

    return Animal.query.filter(Animal.animal_name == animal_name, Animal.organization_animal_id == organization_animal_id).first()

def get_users_favorites_by_user_id(user_id):
    
    return Favorite.query.filter(Favorite.user_id == user_id).all()





if __name__ == "__main__":
    from server import app

    connect_to_db(app)
