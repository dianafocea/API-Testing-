import requests


def get_status():
    response = requests.get('https://simple-books-api.glitch.me/status')
    return response
