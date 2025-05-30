import sqlite3


conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT,
#             password TEXT
#             )''')
# conn.commit()


def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email=?', [email])
    return cur.fetchone()

def new_account(name, email, password):
    cur.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()