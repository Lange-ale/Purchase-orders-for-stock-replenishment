from flask import Flask
from util.db_connection import DBConnection
from model.product_repository import *

class REST_API(Flask):
    def __init__(self, db_conf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = DBConnection(db_conf)
        err = self.db.connect()
        if err:
            print("Error connecting to the database")
            print(err)
            exit(1)
        print("Connected to the database")
        
        
        @self.route('/products_names')
        def index():
            return ProductRepository.get_all_product_names(self.db)
     