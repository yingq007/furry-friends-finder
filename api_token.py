import os
import requests


def get_a_token():

    url = 'https://api.petfinder.com/v2/oauth2/token'

    data = {
        'grant_type':'client_credentials',
        'client_id':os.environ['PETFINDER_API_KEY'], 
        'client_secret':os.environ['PETFINDER_SECRET_KEY']
    }

    res = requests.post(url, data=data)

    info_token_res = res.json()
    print(info_token_res)
    token = info_token_res['token_type'] + ' ' + info_token_res['access_token'] 

    return token




def get_data(url, token, payload):
    headers = {'Authorization': token }
    res = requests.get(url, headers=headers, params=payload)
    data = res.json()
    return data

