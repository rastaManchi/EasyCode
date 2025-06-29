import sqlite3


conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            isadmin INTEGER DEFAULT 0,
            verified  INTEGER DEFAULT 0
            )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT, 
            content TEXT
            )''')
conn.commit()


def add_new_post(title, content):
    cur.execute('INSERT INTO posts(title, content) VALUES (?,?)', [title, content])
    conn.commit()


def get_all_posts():
    cur.execute('SELECT * FROM posts')
    result = cur.fetchall()
    return result


def get_user_by_id(id):
    cur.execute('SELECT * FROM users WHERE id=?', [id])
    return cur.fetchone()

def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email=?', [email])
    return cur.fetchone()

def new_account(name, email, password):
    cur.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()

def verify_account(email):
    cur.execute(f'UPDATE users SET verified = 1 WHERE email = "{email}"')
    conn.commit()

def update_admin(id):
    cur.execute('UPDATE users SET isadmin = 1 WHERE id=?', [id])
    conn.commit()

def get_all_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()

def delete_user_by_id(id):
    cur.execute(f'DELETE FROM users WHERE id = {id}')
    conn.commit()

def user_change(event, data, id):
    if event == 'change_login':
        cur.execute(f'UPDATE users SET name = ? WHERE id=?', [data, id])
    elif event == 'change_email':
        cur.execute(f'UPDATE users SET email = ? WHERE id=?', [data, id])
    elif event == 'change_password':
        cur.execute(f'UPDATE users SET password = ? WHERE id=?', [data, id])
    conn.commit()