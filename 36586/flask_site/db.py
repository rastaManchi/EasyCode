import sqlite3
import secrets
import time


conn = sqlite3.connect('mydb.db', check_same_thread=False)
cur = conn.cursor()


cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT,
                    password TEXT
                )
            """)
conn.commit()


cur.execute("""
                CREATE TABLE IF NOT EXISTS auth_tokens(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token TEXT,
                    user INTEGER,
                    end_date TIMESTAMP,
                    FOREIGN KEY (user) REFERENCES users(id)
                )
            """)
conn.commit()


def create_auth_token(user_id):
    token = secrets.token_urlsafe(32)
    end_date = time.time() + 600
    cur.execute('''INSERT INTO auth_tokens(token, user, end_date)
                VALUES (?, ?, ?)''',
                [token, user_id, end_date])
    conn.commit()
    return token



def validate_auth_token(token):
    cur.execute('''SELECT * FROM auth_tokens WHERE 
                token=? AND end_date>=?''',
                [token, time.time()])
    result = cur.fetchone()
    if result:
        return result[2]
    return False


def get_user_by_email(email):
    cur.execute("SELECT * FROM users WHERE email=?", [email])
    return cur.fetchone() # (1, 'username', 'email', 'password')


def get_user_by_id(user_id):
    cur.execute("SELECT * FROM users WHERE id=?", [user_id])
    return cur.fetchone()


def create_user(username, email, password):
    cur.execute('INSERT INTO users(username, email, password) VALUES (?, ?, ?)',
                [username, email, password])
    conn.commit()