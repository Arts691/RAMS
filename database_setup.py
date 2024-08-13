import sqlite3

def initialize_db():
    conn = sqlite3.connect('road_assets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS roads (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 length REAL,
                 condition TEXT,
                 last_maintenance DATE)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
