import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    ans1 TEXT,
    ans2 TEXT,
    ans3 TEXT,
    ans4 TEXT,
    correct TEXT
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    is_admin INTEGER,
    score INTEGER
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS game_status(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT
    )''')
conn.commit()


def add_user(user_id, is_admin=0, score=0):
    cur.execute('INSERT INTO users(user_id, is_admin, score) VALUES (?, ?, ?)', [user_id, is_admin, score])
    conn.commit()

def get_all_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()

def get_user_by_id(user_id):
    cur.execute('SELECT * FROM users WHERE user_id=?', [user_id])
    return cur.fetchone()

def get_all_questions():
    cur.execute('SELECT * FROM questions')
    return cur.fetchall()

def add_question(text, ans1, ans2, ans3, ans4, correct):
    cur.execute('INSERT INTO questions(text, ans1, ans2, ans3, ans4, correct) VALUES (?, ?, ?, ?, ?, ?)', [text, ans1, ans2, ans3, ans4, correct])
    conn.commit()
    
def change_game_status(status):
    cur.execute('UPDATE game_status SET status=?', [status])
    conn.commit()