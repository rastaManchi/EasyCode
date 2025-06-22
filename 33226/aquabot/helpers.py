import sqlite3

conn = sqlite3.connect('slides.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS slides(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            length INTEGER,
            description TEXT
            )''')
conn.commit()


def get_all_slides():
    cur.execute('SELECT * FROM slides')
    result = cur.fetchall()
    return result

# [(0, name, 5, description), (), ()]