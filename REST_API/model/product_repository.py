class ProductRepository:
    @staticmethod
    def get_all_product_names(db):
        db.cur.execute("SELECT id, name FROM product")
        return db.cur.fetchall()