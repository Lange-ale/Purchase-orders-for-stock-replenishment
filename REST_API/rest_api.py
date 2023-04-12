from flask import Flask
from util.db_connection import DBConnection
from model.product_repository import *
from model.stock_repository import *
from time import sleep

class REST_API(Flask):
    def __init__(self, db_conf, *args, **kwargs):
        super().__init__(*args, **kwargs) # Flask constructor
        self.db = DBConnection(db_conf) # init db conf
        err = self.db.connect() # try to connect to the db
        while err is not None: # if connection fails, try again
            print("Error connecting to the database") 
            print(err)
            sleep(1) 
            err = self.db.connect() 
        print("Connected to the database")
        
        # this uri returns a welcome message
        @self.route('/')
        def index():
            return "Welcome to the REST API of the suppliers' products"
        
        # this uri returns all the products' names
        @self.route('/products_names', methods=['GET'])
        def products_names():
            return ProductRepository.get_all_product_names(self.db)
        
        # this uri returns all the stocks of the product sold by the supplier
        @self.route('/stocks/<int:product_id>/<int:quantity>', methods=['GET'])
        def product_discounts(product_id, quantity):
            return StockRepository.get_stocks_discounts(self.db, product_id, quantity)
        
     
