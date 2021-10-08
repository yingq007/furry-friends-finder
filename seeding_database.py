"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import server
import model

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

# Load dog  data from JSON file
with open("data/dog_data.json") as f:
    dog_data = json.loads(f.read())

# Create animals
animals_in_db = []
for animal in animal_data:
    type, species, gender = (
        animal["type"],
        animal["species"],
        animal["gender"],
    )

    db_animal = crud.create_aniaml(type, species, gender)
    animals_in_db.append(db_animal)

# # Create 10 users; each user will make 10 ratings
# for n in range(10):
#     email = f"user{n}@test.com"  # Voila! A unique email!
#     password = "test"

#     user = crud.create_user(email, password)

#     for _ in range(10):
#         random_movie = choice(movies_in_db)
#         score = randint(1, 5)

#         crud.create_rating(user, random_movie, score)
