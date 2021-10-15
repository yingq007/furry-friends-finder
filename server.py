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
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/animals?type=dog&location=95014&sort=distance'
  
    payload = {
        #'sort': 'distance',
    }
    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}
    print (data)

    for animal in data['animals']:
        if animal['photos']:
            result['dogs'].append(animal)
    return render_template("homepage.html",result=result) 

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
def show_all_animals_api():
    token = api_token.get_a_token()
    url = 'https://api.petfinder.com/v2/animals?type=dog'

    # url = 'https://api.petfinder.com/v2/organizations'
    


    # payload = {
    #     'location':'95014'
    # }
    payload = {
        'type': 'dog'
    }
    data = api_token.get_data(url, token, payload)
    result={'dogs':[]}
    print("************************")
    print(data)
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
    print(result['dogs'][0]['photos'])
    print(result['dogs'][0]['name'])
    return render_template("animals.html", result=result) 

@app.route("/breeds")   
def view_all_breeds():
    
    return render_template("breeds.html", breed=breed, breed_id=breed_id)


@app.route("/search")   
def show_search_form():
   
    
    return render_template("search.html") 


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
            #print(organization_name)
    
    
    
    # return result
    return render_template("search_dogs.html", result=result) 






if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)