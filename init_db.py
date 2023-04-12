from REST_API.util.db_connection import DBConnection
from db.example_data import example_data, example_product_id_1

PRODUCTION_DB =  {
    "host": "localhost",
    "database": "db",
    "user": "user",
    "password": "password",
    "port": "54320"
}

TEST_DB =  {
    "host": "localhost",
    "database": "db-test",
    "user": "test",
    "password": "test",
    "port": "54321"
}


# executes the queries to delete the tables if they exist and create them as defined in the ER diagram
def delete_and_create_tables(conn): 
    cur = conn.cursor()
    
    cur.execute("""DROP TABLE IF EXISTS discount_time_based;
                   DROP TABLE IF EXISTS discount_tot_cost_based;
                   DROP TABLE IF EXISTS discount_n_pcs_based;
                   DROP TABLE IF EXISTS stock;
                   DROP TABLE IF EXISTS product;
                   DROP TABLE IF EXISTS supplier;""")
    
    cur.execute("""CREATE TABLE supplier (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL UNIQUE,
        address VARCHAR(255),
        phone VARCHAR(40),
        email VARCHAR(255)
    );""")
    
    cur.execute("""CREATE TABLE product (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL UNIQUE,
        description text
    );""")
    
    cur.execute("""CREATE TABLE stock (
        id SERIAL PRIMARY KEY NOT NULL,
        id_supplier INTEGER NOT NULL,
        id_product INTEGER NOT NULL,
        quantity INTEGER DEFAULT 0,
        price INTEGER NOT NULL,
        shipping_time INTEGER NOT NULL,
        
        CONSTRAINT fk_supplier
            FOREIGN KEY (id_supplier)
            REFERENCES supplier (id)
            ON DELETE CASCADE,
        CONSTRAINT fk_product
            FOREIGN KEY (id_product)
            REFERENCES product (id)
            ON DELETE CASCADE
    );""")
    
    cur.execute("""CREATE TABLE discount_n_pcs_based (
        id SERIAL PRIMARY KEY NOT NULL,
        id_stock INTEGER NOT NULL,
        min_quantity INTEGER NOT NULL,
        discount_percentage INTEGER NOT NULL,
        
        CONSTRAINT fk_stock
            FOREIGN KEY (id_stock)
            REFERENCES stock (id)
            ON DELETE CASCADE
    );""")
    
    cur.execute("""CREATE TABLE discount_tot_cost_based (
        id SERIAL PRIMARY KEY NOT NULL,
        id_stock INTEGER NOT NULL,
        min_tot_cost INTEGER NOT NULL,
        discount_percentage INTEGER NOT NULL,
        
        CONSTRAINT fk_stock
            FOREIGN KEY (id_stock)
            REFERENCES stock (id)
            ON DELETE CASCADE
    );""")
    
    cur.execute("""CREATE TABLE discount_time_based (
        id SERIAL PRIMARY KEY NOT NULL,
        id_stock INTEGER NOT NULL,
        date_start DATE NOT NULL,
        date_end DATE NOT NULL,
        discount_percentage INTEGER NOT NULL,
        
        CONSTRAINT fk_stock
            FOREIGN KEY (id_stock)
            REFERENCES stock (id)
            ON DELETE CASCADE
    );""")

    conn.commit()    

# takes the example data and inserts it into the database
def insert_example_data(conn):
    cur = conn.cursor()
    
    # insert the only product in the example data
    cur.execute(f"""INSERT INTO product (name, description) VALUES
                ('{example_product_id_1["name"]}', '{example_product_id_1["description"]}');""")
     
    id = 1 # in the loop coincide with the id of the supplier and his stock
    for supplier in example_data: # insert the suppliers, their stock and their discounts
        s = supplier["supplier"]
        cur.execute(f"""INSERT INTO supplier (name, address, phone, email) VALUES 
                    ('{s["name"]}', '{s["address"]}', '{s["phone"]}', '{s["email"]}');""")
        st = supplier["stock"]
        cur.execute(f"""INSERT INTO stock (id_supplier, id_product, quantity, price, shipping_time) VALUES
                    ({id}, 1, {st["quantity"]}, {st["price"]}, {st["shipping_time"]});""")
        if "discount_n_pcs_based" in supplier:
            for discount in supplier["discount_n_pcs_based"]:
                cur.execute(f"""INSERT INTO discount_n_pcs_based (id_stock, min_quantity, discount_percentage) VALUES
                            ({id}, {discount["min_quantity"]}, {discount["discount_percentage"]});""")
        if "discount_tot_cost_based" in supplier:
            for discount in supplier["discount_tot_cost_based"]:
                cur.execute(f"""INSERT INTO discount_tot_cost_based (id_stock, min_tot_cost, discount_percentage) VALUES
                            ({id}, {discount["min_tot_cost"]}, {discount["discount_percentage"]});""")
        if "discount_time_based" in supplier:
            for discount in supplier["discount_time_based"]:
                cur.execute(f"""INSERT INTO discount_time_based (id_stock, date_start, date_end, discount_percentage) VALUES
                            ({id}, '{discount["date_start"]}', '{discount["date_end"]}', {discount["discount_percentage"]});""")
        id += 1
    
    conn.commit()
    

production_db = DBConnection(PRODUCTION_DB)
err = production_db.connect()
if err:
    print("Error connecting to the production database")
    print(err)
    exit(1)
print("Connected to the production database")

testing_db = DBConnection(TEST_DB)
err = testing_db.connect()
if err:
    print("Error connecting to the testing database")
    print(err)
    exit(1)
print("Connected to the testing database")

print("Initializing production database...")
delete_and_create_tables(production_db.conn)
insert_example_data(production_db.conn)
print("""Production database initialized.
Initializating test database...""")
delete_and_create_tables(testing_db.conn)
insert_example_data(testing_db.conn)   
print("Test database initialized.")