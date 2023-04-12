from util.db_connection import DBConnection
from conf.conf_external_docker import production_conf, testing_conf
import unittest

class TestDBConnection(unittest.TestCase):
    # test if the connection to the production database is successful
    def test_production_db_connection(self):
        db = DBConnection(production_conf)
        self.assertIsNone(db.connect())
    
    # test if the connection to the testing database is successful
    def test_testing_db_connection(self):
        db = DBConnection(testing_conf)
        self.assertIsNone(db.connect())
    
    # test if the connection to the production database with wrong credentials fails
    def test_production_db_connection_failure(self):
        wrong_conf = production_conf.copy()
        wrong_conf["password"] = "wrong_password"
        db = DBConnection(wrong_conf)
        self.assertIsNotNone(db.connect())
    
    # test if the connection to the testing database with wrong credentials fails
    def test_testing_db_connection_failure(self):
        wrong_conf = testing_conf.copy()
        wrong_conf["password"] = "wrong_password"
        db = DBConnection(wrong_conf)
        self.assertIsNotNone(db.connect())
