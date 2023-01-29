from books.requests_api.status import *

class TestStatus:

    def test_status_200(self):
        assert get_status().status_code == 200, 'Actual status code is not correct'
        assert get_status().json()['status'] == 'OK', 'Actual status msg is not correct'