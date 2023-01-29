import requests
import json
import pytest
from books.requests_api.orders import *
from books.requests_api.api_clients import *

class TestOrders:
    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        response = add_order(self.token, 2, 'Diana')
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'This book is not in stock. Try again later.', 'The error is incorrect'

    def test_add_valid_order(self):
        response = add_order(self.token, 1, 'Diana')
        assert response.status_code == 201, 'Status code is incorrect'
        assert response.json()['created'] is True, 'Order not created'
        # cleanup
        delete_order(self.token, response.json()['orderId'])

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'user1')
        add2 = add_order(self.token, 4, 'user2')
        response = get_orders(self.token)
        assert response.status_code == 200, 'Status code is incorrect'
        assert len(response.json()) == 2, 'Total of orders returned is incorrect'
        # cleanup
        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token, 4, "Diana")
        response = delete_order(self.token, add.json()['orderId'])
        assert response.status_code == 204, 'Status code is not OK'
        # verify if order is deleted
        verify = get_orders(self.token)
        assert len(verify.json()) == 0, 'Order was not deleted'

    def test_get_one_order(self):
        order = add_order(self.token, 1, 'DiaAnna').json()['orderId']
        response = get_order(self.token, order)
        assert response.status_code == 200, 'Status code is not OK'
        # verify keys
        assert response.json()['id'] == order, 'id is not OK'
        assert response.json()['bookId'] == 1, 'bookId is not OK'
        assert response.json()['customerName'] == 'DiaAnna', 'customerName is not OK'
        assert response.json()['quantity'] == 1, 'quantity is not OK'
        # cleanup
        delete_order(self.token, order)

    def test_delete_invalid_orderId(self):
        response = delete_order(self.token, 'querty5')
        assert response.status_code == 404, 'Status code is not OK'
        assert response.json()['error'] == 'No order with id querty5.', 'The error returned is not correct'

    def test_get_order_invalid_id(self):
        response = get_order(self.token, 'e455e4')
        assert response.status_code == 404, 'Status code is not OK'
        assert response.json()['error'] == 'No order with id e455e4.', 'The error returned is not correct'

    def test_edit_invalid_orderId(self):
        response = edit_order(self.token, '4d5y7r', 'Dia')
        assert response.status_code == 404, 'Status code is not OK'
        assert response.json()['error'] == 'No order with id 4d5y7r.', 'The error returned is not correct'

    def test_edit_orderId(self):
        order = add_order(self.token, 1, 'Diana').json()['orderId']
        response = edit_order(self.token, order, 'Anaid')
        assert response.status_code == 204, 'Status code is not OK'
        get = get_order(self.token, order)
        assert get.json()['customerName'] == 'Anaid', 'Customer name was not updated'
        #cleanup
        delete_order(self.token, order)
















