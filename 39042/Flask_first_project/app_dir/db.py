import sqlite3


db = sqlite3.connect('database.db', check_same_thread=False)
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    is_admin INT DEFAULT 0
)''')
db.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            author INT,
            status INT DEFAULT 0
)''')
db.commit()


def add_new_post(title, content, author_id):
    cur.execute('INSERT INTO posts(title, content, author) VALUES (?, ?, ?)', [title, content, author_id])
    db.commit()
    

def get_all_posts():
    cur.execute('SELECT * FROM posts WHERE status=1')
    return cur.fetchall()


def add_user(name, email, password):
    cur.execute('''INSERT INTO users(name, email, password) VALUES (?, ?, ?)''', [name, email, password])
    db.commit()

def get_user_by_id(id):
    cur.execute(f'SELECT * FROM users WHERE id = {id}')
    return cur.fetchone()

def get_user_by_email(email):
    cur.execute(f'SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()


def delete_post_by_id(id):
    cur.execute(f"DELETE FROM posts WHERE id={id}")
    db.commit()
    
    
def search_post(text):
    cur.execute("""SELECT * FROM posts WHERE status=1 AND (title LIKE
                :keyword OR content LIKE
                :keyword)""", {'keyword': f'%{text}%'})
    return cur.fetchall() 


def get_notchecked_posts():
    cur.execute("SELECT * FROM posts WHERE status=0")
    return cur.fetchall()


def change_post_status(post_id, status):
    cur.execute(f"UPDATE posts SET status={status} WHERE id={post_id}")
    db.commit()
    

def add_admin(id):
    cur.execute(f"UPDATE users SET is_admin=1 WHERE id={id}")
    db.commit()


