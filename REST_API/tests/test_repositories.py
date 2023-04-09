from util.db_connection import DBConnection
from conf.conf import testing_conf
from model.product_repository import *
import unittest

class TestRepositories(unittest.TestCase):
    def test_get_all_products(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
        right_res = [(1, "Philips monitor 17”")]
        res = ProductRepository.get_all_product_names(db)
        self.assertEqual(res, right_res)        