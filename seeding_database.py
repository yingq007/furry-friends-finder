"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import server
import model

os.system("dropdb furry_friends_finder")
os.system("createdb furry_friends_finder")

model.connect_to_db(server.app)
model.db.create_all()

for n in range(1,11):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password)


