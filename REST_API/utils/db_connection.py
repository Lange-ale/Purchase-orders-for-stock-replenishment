from psycopg2 import connect

class DBConnection:
    def __init__(self, conf, is_testing=False):
        self.conf = conf
        
    def connect(self): # connect to the database and return the error if any
        try:
            self.conn = connect(**self.conf)
            self.cur = self.conn.cursor()
        except Exception as e:
            return e
        return None