from books.requests_api.api_clients import *

class TestApiClient:
    nr = randint(1, 9999999)
    clientName = 'Diana2'
    clientEmail = f'dia_mailtest2{nr}@mailinator.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

    def test_successful_login(self):
        assert self.response.status_code == 201, 'Actual status code is incorrect'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in the response'

    def test_login_client_already_registered(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'API client already registered. ' \
        'Try a different email.', 'Wrong message error was returned'

    def test_invalid_or_missing_client_name(self):
        self.response = login("5", "email")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_invalid_or_missing_email(self):
        self.response = login("bad_format", "13@.")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'
