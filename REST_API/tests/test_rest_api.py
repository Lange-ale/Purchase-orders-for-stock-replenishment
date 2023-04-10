import unittest
import requests
from tests.test_rest_api_results import *

class TestRestApi(unittest.TestCase):
    def test_get_products_names(self):
        response = requests.get("http://localhost:5001/products_names")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), right_ans_test_api_get_products_names)
        
    def test_get_product_description(self):
        response = requests.get("http://localhost:5001/product_description/1")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), right_ans_test_get_product_description)
        
    def test_get_product_discounts(self):
        response = requests.get("http://localhost:5001/product_discounts/1")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), right_ans_test_get_product_discounts)