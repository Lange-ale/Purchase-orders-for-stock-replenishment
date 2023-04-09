class ProductRepository:
    @staticmethod
    def get_all_product_names(db):
        db.cur.execute("SELECT id, name FROM product")
        return db.cur.fetchall()
    
    @staticmethod
    def get_product_description(db, product_id):
        db.cur.execute(f"SELECT description FROM product WHERE id = {product_id}")
        return { "description": db.cur.fetchone()[0] }