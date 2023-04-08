from utils.db_connection import DBConnection
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
        db = DBConnection(production_conf)
        db.conf['password'] = 'wrong_password'
        self.assertIsNotNone(db.connect())
    
    def test_testing_db_connection_failure(self):
        db = DBConnection(testing_conf, is_testing=True)
        db.conf['password'] = 'wrong_password'
        self.assertIsNotNone(db.connect())
