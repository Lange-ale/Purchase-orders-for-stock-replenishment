class ProductRepository:
    @staticmethod
    def get_all_product_names(db): # returns a list of tuples (id, name)
        db.cur.execute("SELECT id, name FROM product")
        return db.cur.fetchall()
    
    @staticmethod
    def get_product_description(db, product_id): # returns a dict { "product_description": description }
        db.cur.execute(f"SELECT description FROM product WHERE id = {product_id}")
        return { "product_description": db.cur.fetchone()[0] }