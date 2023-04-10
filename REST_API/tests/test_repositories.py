from util.db_connection import DBConnection
from conf.conf import testing_conf
from model.product_repository import *
from model.discount_repository import *
from tests.test_rest_api_results import *
import unittest

class TestRepositories(unittest.TestCase):
    def test_get_all_products_names(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        res = ProductRepository.get_all_product_names(db)
        self.assertListEqual(res, right_ans_test_repositoory_get_products_names)
        
    def test_get_product_description(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        res = ProductRepository.get_product_description(db, 1)
        self.assertDictEqual(res, right_ans_test_get_product_description)
        
    def test_get_stocks_discounts(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        res = DiscountRepository.get_stocks_discounts(db, 1)
        self.assertDictEqual(res, right_ans_test_get_product_discounts)
         