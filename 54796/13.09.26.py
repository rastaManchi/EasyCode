import sqlite3


conn = sqlite3.connect("zametki.db")
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS animals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gender TEXT,
        type TEXT
    )
""")
conn.commit()


def add_animal(name, gender, type):
    cur.execute("INSERT INTO animals(name, gender, type) VALUES (?, ?, ?)", [name, gender, type])
    conn.commit()


def get_all_animals():
    cur.execute("SELECT * FROM animals")
    print(cur.fetchall())


def get_all_dogs():
    cur.execute("SELECT * FROM animals WHERE type=?", ['собака'])
    print(cur.fetchall())

get_all_dogs()