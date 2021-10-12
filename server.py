import os
petfinder_api_key= os.environ["PETFINDER_API_KEY"]

from flask import Flask, render_template, request, flash, session, redirect
from random import choice, randint
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

import requests
import api_token

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


API_KEY = os.environ['PETFINDER_API_KEY']
SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html") 

@app.route("/api/breeds")
def search_for_breeds():
    breed_type = 'dog'
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/types/' + breed_type + '/breeds'

    payload = {
        'type': breed_type
    }

    data = api_token.get_data(url, token, payload)
    
    print("************************")
    breed_types ={'breeds':[]}
    for breednames in data['breeds']:
        breed_types['breeds'].append(breednames['name'])
    
        #print(breed_types)
    return breed_types
    
    

    #parse through the data, iterate with for loop, store breed names in a dictionary
    #key will be breeds and the value will be a list of breed names
    # {
    #     'breeds': [breedone, breedtwo]
    # }

    # return jsonify(breeds)


@app.route("/api/animals")
def show_all_animals():
    token = api_token.get_a_token()
    # url = 'https://api.petfinder.com/v2/animals?type=dog'

    url = 'https://api.petfinder.com/v2/organizations'
    


    payload = {
        'location':'95014'
    }

    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}
    print("************************")
    print(data)
    # for animal in data['animals']:
    #     result['dogs'].append(animal)
    
    return 'hello'

    

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
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")
    

    #parse through the data, iterate with for loop, store breed names in a dictionary
    #key will be breeds and the value will be a list of breed names
    # {
    #     'breeds': [breedone, breedtwo]
    # }

    # return jsonify(breeds)

    return render_template("homepage.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)