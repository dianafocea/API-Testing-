from random import randint
import requests


def login(clientName=None, clientEmail=None):
    json = {
        'clientName': clientName,
        'clientEmail': clientEmail
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients', json=json)
    return response
# in def login se returneaza tot raspunsul
# metoda e folosita in api_clients


def get_token():
    nr = randint(1, 9999999)
    json = {
        'clientName': 'Diana',
        'clientEmail': f'valid_emailDIa{nr}@mailinator.com'
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients', json=json)
    return response.json()['accessToken']
# in get_token se returneaza doar valoarea din token
# metoda e folosita in orders
