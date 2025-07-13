import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER,
    email TEXT,
    phone TEXT
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS slides(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    len INTEGER,
    description TEXT
    )''')
conn.commit()

def get_all_slides():
    cur.execute('SELECT * FROM slides')
    return cur.fetchall()


def get_slide_by_name(name):
    cur.execute('SELECT * FROM slides WHERE name=?', [name])
    return cur.fetchone()

