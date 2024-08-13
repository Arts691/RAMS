import sqlite3

def add_road(name, length, condition, last_maintenance):
    conn = sqlite3.connect('road_assets.db')
    c = conn.cursor()
    c.execute('INSERT INTO roads (name, length, condition, last_maintenance) VALUES (?, ?, ?, ?)',
              (name, length, condition, last_maintenance))
    conn.commit()
    conn.close()

def get_all_roads():
    conn = sqlite3.connect('road_assets.db')
    c = conn.cursor()
    c.execute('SELECT * FROM roads')
    roads = c.fetchall()
    conn.close()
    return roads

def update_road(id, name, length, condition, last_maintenance):
    conn = sqlite3.connect('road_assets.db')
    c = conn.cursor()
    c.execute('UPDATE roads SET name=?, length=?, condition=?, last_maintenance=? WHERE id=?',
              (name, length, condition, last_maintenance, id))
    conn.commit()
    conn.close()
