import sqlite3


conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
)''')

conn.commit()

cur.execute(''' CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
)''')

conn.commit()

def add_posts(title, content):
    cur.execute('INSERT INTO posts(title, content) VALUES (?, ?)', [title, content])
    conn.commit()
  

def get_posts():
    cur.execute(f'SELECT * FROM posts')
    return cur.fetchall() # [(1, 'title', 'content'), (2, 'title', 'content')]


def add_user(name, email, password):
    cur.execute('INSERT INTO users(name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()

def get_user_by_id(user_id):
    cur.execute(f'SELECT * FROM users WHERE id = {user_id}')
    return cur.fetchone() # (1, 'Булат', 'admin@admin', 'qwerty')

def get_user_by_email(email):
    cur.execute(f'SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()