import unittest
import requests

class TestRestApi(unittest.TestCase):
    def test_get_products_names(self):
        response = requests.get("http://localhost:5001/products_names")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [[1, "Philips monitor 17”"]])
        
    def test_get_product_description(self):
        response = requests.get("http://localhost:5001/product_description/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"description": "A monitor with a 17” screen"})
    