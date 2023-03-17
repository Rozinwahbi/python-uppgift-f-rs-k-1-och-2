import sqlite3
import os

class DB:
    db_url: str
    
    def __init__(self, db_url: str):
        self.db_url = db_url

        if not os.path.exists(self.db_url):
            self.init_db()
            print("Database initialized.")

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data

    def init_db(self):
        init_db_query = """
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY,
            name text NOT NULL,
            mission text NOT NULL
        );
        """
        insert_query = """
        INSERT INTO todo(name,mission)
        VALUES('mission', 'mission2');
        """
        self.call_db(init_db_query)
        self.call_db(insert_query)
