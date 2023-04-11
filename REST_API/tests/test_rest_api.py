import unittest
import requests
from tests.test_results import *

class TestRestApi(unittest.TestCase):
    def test_api_get_products_names(self):
        response = requests.get("http://localhost:5001/products_names")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), right_ans_test_api_get_products_names)
        
    def test_api_get_1_product_discounts(self):
        response = requests.get("http://localhost:5001/stocks/1/1")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), right_ans_test_get_1_product_discounts)
        
    def test_api_get_12_products_discounts(self):
        response = requests.get("http://localhost:5001/stocks/1/12")
        self.assertEqual(response.status_code, 200)
        right_ans = [right_ans_test_get_1_product_discounts[1],
                     right_ans_test_get_1_product_discounts[2]]
        self.assertListEqual(response.json(), right_ans)
        
    def test_api_get_quantity_not_available(self):
        response = requests.get("http://localhost:5001/stocks/1/100")
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json(), right_ans_test_get_quantity_not_available)