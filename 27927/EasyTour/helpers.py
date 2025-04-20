import sqlite3

conn = sqlite3.connect('tours.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tours(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price INTEGER,
            category TEXT,
            country TEXT,
            days INTEGER,
            likes INTEGER
)''')
conn.commit()

def get_all_tours():
    cur.execute('SELECT * FROM tours')
    return cur.fetchall()


def get_tour_covers():
    cur.execute('SELECT id, name FROM tours')
    return cur.fetchall()

def get_cover_by_id(tour_id):
    cur.execute(f'SELECT id, name FROM tours WHERE id = {tour_id}')