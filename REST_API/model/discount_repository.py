class DiscountRepository:
    @staticmethod
    def get_stocks_discounts(db, product_id):
        sql = f"""
            SELECT supplier.name, supplier.address, supplier.phone, supplier.email, 
                   stock.id, stock.price, stock.quantity, stock.shipping_time,
                   discount_n_pcs_based.min_quantity, discount_n_pcs_based.discount_percentage,
                   discount_tot_cost_based.min_tot_cost, discount_tot_cost_based.discount_percentage, 
                   discount_time_based.date_start, discount_time_based.date_end,
                   discount_time_based.discount_percentage
            FROM stock
            INNER JOIN supplier ON stock.id_supplier = supplier.id
            LEFT JOIN discount_n_pcs_based ON stock.id = discount_n_pcs_based.id_stock
            LEFT JOIN discount_tot_cost_based ON stock.id = discount_tot_cost_based.id_stock
            LEFT JOIN discount_time_based ON stock.id = discount_time_based.id_stock
            WHERE stock.id_product = {product_id}
        """  
   
        db.cur.execute(sql)
        data = db.cur.fetchall()
        stocks = {}

        for row in data:
            id = str(row[4])
            if id not in stocks:
                stocks[id] = {
                    "supplier": {
                        "name": row[0],
                        "address": row[1],
                        "phone": row[2],
                        "email": row[3]
                    },
                    "price": row[5],
                    "quantity": row[6],
                    "shipping_time": row[7],
                    "discount_n_pcs_based": [],
                    "discount_tot_cost_based": [],
                    "discount_time_based": []
                }
            if row[8] is not None: # check if there is a discount_n_pcs_based
                stocks[id]["discount_n_pcs_based"].append({
                    "min_quantity": row[8],
                    "discount_percentage": row[9]
                })
            if row[10] is not None: # check if there is a discount_tot_cost_based
                stocks[id]["discount_tot_cost_based"].append({
                    "min_tot_cost": row[10],
                    "discount_percentage": row[11]
                })
            if row[12] is not None: # check if there is a discount_time_based
                stocks[id]["discount_time_based"].append({
                    "date_start": row[12].strftime("%Y-%m-%d"),
                    "date_end": row[13].strftime("%Y-%m-%d"),                    
                    "discount_percentage": row[14]
                })
                
        return stocks
                
                
                
            