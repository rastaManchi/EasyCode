import sqlite3


db = sqlite3.connect('database.db', check_same_thread=False)
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
)''')
db.commit()


def add_user(name, email, password):
    cur.execute('''INSERT INTO users(name, email, password) VALUES (?, ?, ?)''', [name, email, password])
    db.commit()

def get_user_by_id(id):
    cur.execute(f'SELECT * FROM users WHERE id = {id}')
    return cur.fetchone()

def get_user_by_email(email):
    cur.execute(f'SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()