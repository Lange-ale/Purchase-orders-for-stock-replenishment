from util.db_connection import DBConnection
from conf.conf import testing_conf
from model.product_repository import *
from model.stock_repository import *
from tests.test_results import *
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
        
    def test_get_1_stocks_discounts(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        res = StockRepository.get_stocks_discounts(db, 1, 1)
        self.assertListEqual(res, right_ans_test_get_1_product_discounts)
        
    def test_get_12_stocks_discounts(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        res = StockRepository.get_stocks_discounts(db, 1, 12)
        right_ans = [right_ans_test_get_1_product_discounts[1],
                     right_ans_test_get_1_product_discounts[2]]
        self.assertListEqual(res, right_ans)
    
    def test_get_quantity_not_available(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        res = StockRepository.get_stocks_discounts(db, 1, 100)
        self.assertListEqual(res, right_ans_test_get_quantity_not_available)
         