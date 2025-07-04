import sqlite3


conn = sqlite3.connect('questions.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text_question TEXT,
    ans1 TEXT,
    ans2 TEXT,
    ans3 TEXT,
    ans4 TEXT,
    correct TEXT
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    isadmin INTEGER DEFAULT 0,
    score INTEGER DEFAULT 0
    )''')
conn.commit()

# users
def get_user(user_id):
    cur.execute('SELECT * FROM users WHERE user_id=?', [user_id])
    return cur.fetchone()

def add_user(user_id):
    cur.execute('INSERT INTO users(user_id) VALUES (?)', [user_id])
    conn.commit()

def set_admin(user_id):
    cur.execute('UPDATE users SET isadmin=1 WHERE user_id=?', [user_id])
    conn.commit()

# questions
def get_all_questions():
    cur.execute('SELECT * FROM questions')
    return cur.fetchall()


def add_new_question(text, a1, a2, a3, a4, correct):
    cur.execute('INSERT INTO questions(text_question, ans1, ans2, ans3, ans4, correct) VALUES (?, ?, ?, ?, ?, ?)', [text, a1, a2, a3, a4, correct])
    conn.commit()
    