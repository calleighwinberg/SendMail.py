import pytest
from flask_interface import *
import unittest

class MyTestFlask(unittest.TestCase):
    def test_email_response(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            response = client.post('/email', data={'to': 'mars@calleighwinberg.courses', 'from': 'calleighwinberg@gmail.com',
                                                   'text': '3000'})
            # check result from server with expected data
            self.assertEqual(200, response.status_code)
            print(response.data)



