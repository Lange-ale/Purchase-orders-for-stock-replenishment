from util.db_connection import DBConnection
from conf.conf import *
import unittest

class TestDBConnection(unittest.TestCase):
    def test_production_db_connection(self):
        db = DBConnection(production_conf)
        self.assertIsNone(db.connect())
    
    def test_testing_db_connection(self):
        db = DBConnection(testing_conf, is_testing=True)
        self.assertIsNone(db.connect())
    
    def test_production_db_connection_failure(self):
        wrong_conf = production_conf.copy()
        wrong_conf["password"] = "wrong_password"
        db = DBConnection(wrong_conf)
        self.assertIsNotNone(db.connect())
    
    def test_testing_db_connection_failure(self):
        wrong_conf = testing_conf.copy()
        wrong_conf["password"] = "wrong_password"
        db = DBConnection(wrong_conf, is_testing=True)
        self.assertIsNotNone(db.connect())
