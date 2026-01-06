import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path, schema_path):
        self.db_path = db_path
        self.schema_path = schema_path
        self.conn = None
        self.cursor = None

    def connect(self):
        # Ensure output directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def init_schema(self):
        print(f"Loading schema from {self.schema_path}...")
        with open(self.schema_path, 'r') as f:
            self.conn.executescript(f.read())

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()