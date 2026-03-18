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
            content TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
)''')

conn.commit()


def add_posts(title, content, user_id=1):
    cur.execute('INSERT INTO posts(title, content, user_id) VALUES (?, ?, ?)', [title, content, user_id])
    conn.commit()


def get_posts():
    cur.execute(f'SELECT * FROM posts')
    return cur.fetchall() # [(1, 'title', 'content', 1), (2, 'title', 'content', 2)]


def get_posts_by_user_id(user_id):
    cur.execute('SELECT * FROM posts WHERE user_id=?', [user_id])
    return cur.fetchall()


def add_user(name, email, password):
    cur.execute('INSERT INTO users(name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()

def get_user_by_id(user_id):
    cur.execute(f'SELECT * FROM users WHERE id = {user_id}')
    return cur.fetchone() # (1, 'Булат', 'admin@admin', 'qwerty')

def get_user_by_email(email):
    cur.execute(f'SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()