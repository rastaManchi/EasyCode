import sqlite3

conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    is_admin INTEGER,
    score INTEGER
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    ans1 TEXT,
    ans2 TEXT,
    ans3 TEXT,
    ans4 TEXT,
    correct TEXT
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS game_status(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT
    )''')
conn.commit()


def get_all_questions():
    cur.execute('SELECT * FROM questions')
    return cur.fetchall()