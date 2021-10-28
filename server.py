import os
petfinder_api_key= os.environ["PETFINDER_API_KEY"]

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from random import choice, randint
from model import connect_to_db
import crud
import default_breed_types
from jinja2 import StrictUndefined

import requests
import api_token

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


API_KEY = os.environ['PETFINDER_API_KEY']
SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']
breed_types_global ={'breeds':default_breed_types.breed_types}

@app.route('/')
def homepage():
    """View homepage."""
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/animals?type=dog&location=95014&sort=random'
  
    payload = {
        #'sort': 'random',
    }
    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}

    for animal in data['animals']:
        if animal['photos']:
            result['dogs'].append(animal)

    breed_url = 'https://api.petfinder.com/v2/types/' + 'dog' + '/breeds'
    breed_payload = {
        'type': 'dog'
    }
    breed_data = api_token.get_data(breed_url, token, breed_payload)
    updated_breed_types=[]
    for breednames in breed_data['breeds']:
        updated_breed_types.append(breednames['name'])
        breed_types_global.update({'breeds':updated_breed_types})
    return render_template("homepage.html",result=result) 


@app.route("/api/breeds")
def search_for_breeds():
    breed_type = 'dog'
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/types/' + breed_type + '/breeds'

    payload = {
        'type': breed_type
    }

    # data = api_token.get_data(url, token, payload)
    
    # breed_types ={'breeds':[]}
    # for breednames in data['breeds']:
    #     breed_types['breeds'].append(breednames['name'])
    breed_types=breed_types_global
    return breed_types
    

@app.route("/api/animals")
def show_all_animals_api():
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/animals?type=dog'

    payload = {
        'type': 'dog'
    }
    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}
    for animal in data['animals']:
        result['dogs'].append(animal)
    
    return result


@app.route('/create_user')
def create_user():
    """View create account page"""

    return render_template("create_user.html") 


@app.route("/create_user", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    crud.create_user(email, password)
    flash("Account created! Please log in.")

    return redirect("/")


@app.route('/login')
def login_user():
    """View create account page"""

    return render_template("login.html") 


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}!")

    return redirect("/")


@app.route("/animals")   
def view_all_animals():
    
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/animals?type=dog'
  
    payload = {
        'type': 'dog'
    }
    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}
    for animal in data['animals']:
        if not animal['photos']:
            animal['photos']=[{'large':""}]
            animal['photos'][0]['large']="https://web.mo.gov/doc/PuppiesForParolePublic/images/noPhoto.png"
        result['dogs'].append(animal)
    return render_template("animals.html", result=result) 


@app.route("/breeds")   
def view_all_breeds():
    
    return render_template("breeds.html", breed=breed, breed_id=breed_id)


@app.route("/search")   
def show_search_form():
    # breed_type = 'dog'
    # token = api_token.get_a_token()
    # url = 'https://api.petfinder.com/v2/types/' + breed_type + '/breeds'

    # payload = {
    #     'type': breed_type
    # }

    # data = api_token.get_data(url, token, payload)
    
    # breed_types ={'breeds':[]}
    # for breednames in data['breeds']:
    #     breed_types['breeds'].append(breednames['name'])
    
    return render_template("search.html",breed_types_global=breed_types_global) 


@app.route('/search/dogs')
def search_for_dogs():
    """Search for dogs based on location"""
    token = api_token.get_a_token()
    zipcode = request.args.get("zipcode")
    breed = request.args.get("breed")
    url ='https://api.petfinder.com/v2/animals?' 
    
    payload = {
        'type':'dog',
        'location':'{zipcode}'.format(zipcode=zipcode),
        'breed':'{breed}'.format(breed=breed)
    }  
    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}
    if data['animals']:
        for dog in data['animals']:
            if dog['photos']:
                result['dogs'].append(dog)

    return render_template("search_dogs.html", result=result) 


@app.route('/search_dogs/favorite', methods=["POST"])
def favorite_a_dog():
    """Process favorite a dog."""

    animal_name = request.form.get("animal_name")
    animal_description = request.form.get("aniaml_description")
    spayed_neutered  = request.form.get("spayed_neutered")
    age = request.form.get("age")
    gender = request.form.get("gender")
    primary_breed = request.form.get("primary_breed")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")
    url = request.form.get("url")
    photo = request.form.get("photo")
    organization_animal_id = request.form.get("organization_animal_id")
    
    animal = crud.get_animal_by_animal_name_and_organization_animal_id(animal_name, organization_animal_id)

    if animal is None:
        animal = crud.create_animal(animal_name, animal_description, spayed_neutered, age, gender, primary_breed, email, phone_number, url, photo, organization_animal_id)
    favorite = crud.create_favorite(animal.animal_id, session['user_id'])

    flash(f" You've added to your favorite!")

    return redirect("/")

@app.route('/favorite_dogs')
def show_favorite_dogs():
    
    user = crud.get_user_by_id(session['user_id'])
    favorites = user.animals
    favorites_dictionary ={'favorite':[]}
    for animal in favorites:
        fav_animal={}
        fav_animal['animal_id']= animal.animal_id
        fav_animal['animal_name']= animal.animal_name
        fav_animal['animal_description']= animal.animal_description
        fav_animal['spayed_neutered']= animal.spayed_neutered
        fav_animal['age']=animal.age
        fav_animal['gender']=animal.gender
        fav_animal['primary_breed']=animal.primary_breed
        fav_animal['email']=animal.email
        fav_animal['phone_number']=animal.phone_number
        fav_animal['url']=animal.url
        fav_animal['photo']=animal.photo
        fav_animal['organization_animal_id']=animal.organization_animal_id

        favorites_dictionary['favorite'].append(fav_animal)
    
   
    return jsonify(favorites_dictionary)
    # return render_template("user_profile.html") 
@app.route('/user_profile')
def view_user_profile():
    """View create account page"""

    return render_template("user_profile.html") 


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)