import sqlite3

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
                FOREIGN KEY (user_id) REFERENCES users(id)
                )''')
    conn.commit()

    return conn, cur 

conn, cur = init_db()


def set_admin(user_id):
    cur.execute(f'''UPDATE users SET is_admin = 1
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