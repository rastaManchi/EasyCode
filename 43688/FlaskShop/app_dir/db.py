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
        password TEXT,
        is_admin INTEGER DEFAULT 0
    )        
            ''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        user_id INTEGER,
        status INTEGER DEFAULT 0, 
        FOREIGN KEY (user_id) REFERENCES users(id)
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
        user_id INTEGER,
        token TEXT,
        expires_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )        
            ''')
conn.commit()


cur.execute('''
        CREATE TABLE IF NOT EXISTS api_tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT,
            requests_count INTEGER DEFAULT 0,
            expires_at TIMESTAMP,
            owner INTEGER,
            FOREIGN KEY (owner) REFERENCES users(id)
        )
            ''')
conn.commit()


def create_token(owner):
    token = secrets.token_hex(32)
    expires_at = time.time() + 600
    cur.execute('''INSERT INTO api_tokens(token, expires_at, owner)
                VALUES (?, ?, ?)''', [token, expires_at, owner])
    conn.commit()
    return token


def validate_api_token(token):
    cur.execute(f'''SELECT * FROM api_tokens WHERE token="{token}" 
                AND expires_at >= {time.time()}''')
    result = cur.fetchone()
    if result:
        return True
    return False


def add_api_request(token):
    cur.execute(f'''UPDATE api_tokens SET requests_count=requests_count+1
                WHERE token="{token}" ''')
    conn.commit()


def create_auth_token(user_id, remember=False):
    token = secrets.token_hex(32)
    if remember:
        expires_at = time.time() + 60 * 60 * 24 * 30
    else:
        expires_at = time.time() + 60 * 60
    cur.execute('INSERT INTO auth_tokens(user_id, token, expires_at) VALUES (?, ?, ?)', [user_id, token, expires_at])
    conn.commit()
    return token


def validate_auth_token(token):
    cur.execute('SELECT user_id FROM auth_tokens WHERE token=? AND expires_at > ?', [token, time.time()])
    result = cur.fetchone()
    if result:
        return result[0]
    return None


def log_notification(user_id, action, details):
    cur.execute('INSERT INTO notifications(user_id, action, details) VALUES (?, ?, ?)', [user_id, action, details])
    conn.commit()
    
    
def get_notifications_by_user_id(user_id):
    cur.execute(f'SELECT * FROM notifications WHERE user_id={user_id} ORDER BY created_at DESC')
    return cur.fetchall()


def get_all_posts():
    cur.execute('SELECT * FROM posts ORDER BY id DESC')
    return cur.fetchall() # [ (1, 'Название', 'Контент'),  (2, 'Название', 'Контент') ]


def get_status_posts(status):
    cur.execute(f'SELECT * FROM posts WHERE status={status}')
    return cur.fetchall()

def set_post_status(id, status):
    cur.execute(f'UPDATE posts SET status={status} WHERE id={id}')
    conn.commit()

def get_all_posts_by_page(limit, offset):
    cur.execute('''SELECT * FROM posts ORDER BY id DESC
                LIMIT ? OFFSET ?''', [limit, offset])
    return cur.fetchall()


def get_posts_by_text(text):
    cur.execute(f'''
                SELECT * FROM posts
                WHERE title LIKE "%{text}%" OR 
                content LIKE "%{text}%"
                ORDER BY id DESC
                ''')
    return cur.fetchall()


def get_posts_count():
    cur.execute("SELECT COUNT(*) FROM posts")
    return cur.fetchone()[0]


def get_posts_by_user_id(user_id):
    cur.execute(f'''SELECT * FROM posts
                    WHERE user_id={user_id}
                    ORDER BY id DESC''')
    return cur.fetchall() 


def update_post(post_id, title, content):
    cur.execute('UPDATE posts SET title=?, content=? WHERE id=?', [title, content, post_id])
    conn.commit()


def get_post_by_id(post_id):
    cur.execute(f'SELECT * FROM posts WHERE id={post_id}')
    return cur.fetchone()


def add_user(name, email, password):
    cur.execute('''
        INSERT INTO users(name, email, password) VALUES
        (?, ?, ?)
                ''', [name, email, password])
    conn.commit()
    
    
def add_new_post(title, content, user_id=1):
    cur.execute('''
        INSERT INTO posts(title, content, user_id) VALUES
        (?, ?, ?)
                ''', [title, content, user_id])
    conn.commit()    
    

def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email=?', [email])
    return cur.fetchone() # (1, 'Булат', '@mail.ru', '123')


def get_user_by_id(id):
    if id:
        cur.execute(f'SELECT * FROM users WHERE id={id}')
        return cur.fetchone() # (1, 'Булат', '@mail.ru', '123')
    return False

def get_all_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()


def set_isadmin(status, id):
    cur.execute(f'UPDATE users SET is_admin={status} WHERE id={id}')
    conn.commit()
    
    
set_isadmin(True, 1)
