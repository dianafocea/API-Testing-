import pytest

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

    def test_invalid_client_name(self):
        self.response = login("", "test@email.com")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_invalid_email_test1(self):
        self.response = login("test_", "13")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_invalid_email_test2(self):
        self.response = login("test", "test@")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_invalid_email_test3(self):
        self.response = login("test_", "test@domain")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_invalid_email_test4(self):
        self.response = login("test", ".test")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_invalid_email_test5(self):
        self.response = login("test", "test.com")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_invalid_login_credentials(self):
        self.response = login("3", "6")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_missing_client_name(self):
        self.response = login("", "test@e.com")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    def test_missing_email(self):
        self.response = login("login4", "")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'

    def test_missing_login_credentials(self):
        self.response = login("", "")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'

    param = [
        ('', 'test@email.com'),
        ('return_eroare!', 't'),
        ('return_eroare!', 'test@email.com'),
        ('2', 'test.com'),
        ('tst', 'test.'),
        ('2', 'test.com'),
        (' ', 'test@domain'),
        ('!', 'test@')

    ]

    @pytest.mark.parametrize('username, user_email', param)
    def test_invalid_email_param(self, username, user_email):
        self.response = login("username", "user_email")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'Wrong message error was returned'


    def test_invalid_client_n2ame(self):
        self.response = login("return_eroare", "test@email.com")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'
    def test_invalid_client_n3ame(self):
        self.response = login("return_eroare", "t")
        assert self.response.status_code == 400, 'Actual status code is incorrect'
        assert self.response.json()['error'] == 'Invalid or missing client name.', 'Wrong message error was returned'
