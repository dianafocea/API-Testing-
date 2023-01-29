import requests


def get_books(limit='', book_type=''):
    return requests.get(f'https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}')


def get_book(book_id):
    return requests.get(f'https://simple-books-api.glitch.me/books/{book_id}')
