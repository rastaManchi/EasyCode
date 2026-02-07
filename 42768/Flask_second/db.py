import sqlite3


conn = sqlite3.connect('mydb.db', check_same_thread=False)
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT
    )""")
conn.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )""")
conn.commit()


def add_post_to_db(title, content):
    cur.execute('INSERT INTO posts(title, content) VALUES (?, ?, ?)', [title, content])
    conn.commit()


# 1. TODO: добавить функцию получения всех постов


def add_user(name, email, password):
    cur.execute('INSERT INTO users(name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()
    
def get_user_by_id(id):
    cur.execute(f'SELECT * FROM users WHERE id={id}')
    return cur.fetchone() # (1, 'Булат', '123@123', 'qwerty')

def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email=?', [email])
    return cur.fetchall() # [ (1, 'Булат', '123@123', 'qwerty') ]
    