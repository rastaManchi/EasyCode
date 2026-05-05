import sqlite3


conn = sqlite3.connect('mydb.db', check_same_thread=False)
cur = conn.cursor()


cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT
            )
            ''')
conn.commit()


def get_user_by_id(user_id):
    cur.execute('SELECT * FROM users WHERE id=?', [user_id])
    return cur.fetchone() # (1, 'Булат', 'admin@admin', 'qwerty')


def get_user_by_email(user_email):
    cur.execute(f'SELECT * FROM users WHERE email="{user_email}" ')
    return cur.fetchone()


def create_user(user_name, user_email, user_password):
    cur.execute('''INSERT INTO users(name, email, password)
                VALUES (?, ?, ?)''', [user_name, user_email, user_password])
    conn.commit()
