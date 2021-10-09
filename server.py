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
    print(data)

    #parse through the data, iterate with for loop, store breed names in a dictionary
    #key will be breeds and the value will be a list of breed names
    # {
    #     'breeds': [breedone, breedtwo]
    # }

    # return jsonify(breeds)

    return render_template("homepage.html")

# @app.route("/animals")
# def show_all_animals():
#     """View all animals"""
#     gender = request.args.get('gender', '')
   
   

#     url = 'https://api.petfinder.com/v2/animals?type=dog'



#     return render_template("all_animals.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)