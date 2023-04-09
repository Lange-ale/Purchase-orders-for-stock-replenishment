import unittest
import requests

class TestRestApi(unittest.TestCase):
    def test_rest_api(self):
        response = requests.get('http://localhost:5001/products_names')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [[1, 'Philips monitor 17”']])