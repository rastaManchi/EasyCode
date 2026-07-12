import sqlite3
import secrets
import time


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


cur.execute('''
            CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                author INTEGER,
                FOREIGN KEY (author) REFERENCES users(id)
            )
            ''')
conn.commit()


cur.execute('''
            CREATE TABLE IF NOT EXISTS notifications(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            ''')
conn.commit()


cur.execute('''
            CREATE TABLE IF NOT EXISTS auth_tokens(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT,
                user_id INTEGER,
                expires_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            ''')
conn.commit()


cur.execute('''
            CREATE TABLE IF NOT EXISTS api_tokens(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT,
                user_id INTEGER,
                expires_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            ''')
conn.commit()



def create_api_token(user_id):
    token = secrets.token_hex(32)
    expires_at = time.time() + 600
    cur.execute('''INSERT INTO api_tokens(token, user_id, expires_at)
                VALUES (?, ?, ?)''', [token, user_id, expires_at])
    conn.commit()
    return token


def validate_api_token(token):
    cur.execute('''SELECT * FROM api_tokens
                WHERE token=? AND expires_at>?''', [token, time.time()])
    result = cur.fetchone()
    if result:
        return True
    return False


def create_auth_token(user_id):
    token = secrets.token_hex(32)
    expires_at = time.time() + 600
    cur.execute('''INSERT INTO auth_tokens(token, user_id, expires_at)
                VALUES (?, ?, ?)''', [token, user_id, expires_at])
    conn.commit()
    return token


def validate_auth_token(token):
    cur.execute('''SELECT * FROM auth_tokens
                WHERE token=? AND expires_at>?''', [token, time.time()])
    result = cur.fetchone()
    if result:
        return result[2]
    return 0


def add_log_notification(user_id, action, details):
    cur.execute('''INSERT INTO notifications(user_id, action, details)
                VALUES (?, ?, ?)''', [user_id, action, details])
    conn.commit()
    
    
def get_logs_notifications_by_user(user_id):
    cur.execute('SELECT * FROM notifications WHERE user_id=?', [user_id])
    return cur.fetchall()


def get_all_posts():
    cur.execute('SELECT * FROM posts')
    return cur.fetchall() # [(1, 'title', 'content', 1), (2, 'title', 'content', 1)]


def create_post(title, content, author=1):
    cur.execute('''INSERT INTO posts(title, content, author)
                VALUES (?, ?, ?)''', [title, content, author])
    conn.commit()
    

def get_posts_by_user(user_id):
    cur.execute('SELECT * FROM posts WHERE author=?',
                [user_id])
    return cur.fetchall()


def get_user_by_id(user_id):
    cur.execute('SELECT * FROM users WHERE id=?', [user_id])
    return cur.fetchone() # (1, 'Булат', 'admin@admin', 'qwerty')


def get_user_by_email(user_email):
    cur.execute(f'SELECT * FROM users WHERE email="{user_email}" ')
    return cur.fetchone()


def get_all_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()


def create_user(user_name, user_email, user_password):
    cur.execute('''INSERT INTO users(name, email, password)
                VALUES (?, ?, ?)''', [user_name, user_email, user_password])
    conn.commit()
