import sqlite3
import os

def init_db():
    database_path = os.path.join(os.path.dirname(__file__), 'instance/tourdeflask.sqlite')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    schema_path = os.path.join(os.path.dirname(__file__), 'app/schema.sql')
    with open(schema_path, 'r') as f:
        cursor.executescript(f.read())

    connection.commit()
    connection.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")