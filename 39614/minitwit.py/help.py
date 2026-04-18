import sqlite3
import secrets
import time


def init_db():
    conn = sqlite3.connect('users.db', check_same_thread= False)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT,
                is_admin INTEGER DEFAULT 0
                )''')
    conn.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                user_id INTEGER,
                status INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
                )''')
    conn.commit()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS auth_tokens(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT,
                user_id INTEGER,
                expires_at TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
                )''')
    conn.commit()

    return conn, cur 

conn, cur = init_db()


def create_token(user_id, remember=False):
    token = secrets.token_hex(32)
    if remember:
        expires_at = time.time() + 60 * 10
    else:
        expires_at = time.time() + 10
    cur.execute('INSERT INTO auth_tokens(token, user_id, expires_at) VALUES (?, ?, ?)', [token, user_id, expires_at])
    conn.commit()
    return token


def validate_token(token):
    cur.execute('SELECT user_id FROM auth_tokens WHERE token=? AND expires_at>?', [token, time.time()])
    result = cur.fetchone()
    if result:
        return result[0]
    return None


def set_admin(status, user_id):
    cur.execute(f'''UPDATE users SET is_admin = {status}
                    WHERE id={user_id}''')
    conn.commit()


def add_user(name, email, password):
    cur.execute('INSERT INTO users(name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()
    
def add_new_post(title, content, user_id):
    cur.execute('INSERT INTO posts(title, content, user_id) VALUES (?, ?, ?)', [title, content, user_id])
    conn.commit()

def get_all_posts():
    cur.execute('SELECT * FROM posts')
    return cur.fetchall()


def get_all_posts_by_page(limit, offset):
    cur.execute('''SELECT * FROM posts
                LIMIT ? OFFSET ?''', [limit, offset])
    return cur.fetchall()

def get_posts_count():
    cur.execute("SELECT COUNT(*) FROM posts")
    return cur.fetchone()[0]


def get_all_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()


def get_posts_by_user_id(user_id):
    cur.execute('SELECT * FROM posts WHERE user_id = ?', [user_id])
    return cur.fetchall()

def get_user_by_id(user_id):
    cur.execute('SELECT * FROM users WHERE id = ?', [user_id])
    return cur.fetchone()

def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()


def search_posts_by_text(search_text):
    cur.execute('''SELECT * FROM posts 
                WHERE title LIKE ? OR content LIKE ?''',
                [f"%{search_text}%", f"%{search_text}%"])
    return cur.fetchall()


def get_posts_by_status(status):
    cur.execute(f'SELECT * FROM posts WHERE status={status}')
    return cur.fetchall()

def set_post_status(status, id):
    cur.execute(f'UPDATE posts SET status={status} WHERE id={id}')
    conn.commit()
    
    
def update_post(post_id, title, content):
    cur.execute('UPDATE posts SET title=?, content=? WHERE id=?', [title, content, post_id])
    conn.commit()
    
def get_post_by_id(post_id):
    cur.execute(f'SELECT * FROM posts WHERE id={post_id}')
    return cur.fetchone()
