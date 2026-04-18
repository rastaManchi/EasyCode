import sqlite3


db = sqlite3.connect('sqlite.db', check_same_thread=False)
cur = db.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )''')
db.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        author_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES users(id)
    )''')
db.commit()


def add_post(title, content, author_id=1):
    cur.execute('INSERT INTO posts(title, content, author_id) VALUES (?, ?, ?)', [title, content, author_id])
    db.commit()
    

def get_posts():
    cur.execute('SELECT * FROM posts')
    return cur.fetchall() # [(1, 'title', 'content'), (2, 'title', 'content')]


def get_posts_by_author(author_id=1):
    cur.execute(f'SELECT * FROM posts WHERE author_id={author_id}')
    return cur.fetchall()


def create_user(username, email, password):
    cur.execute('''INSERT INTO users(username, email, password)
                VALUES (?, ?, ?)''', [username, email, password])
    db.commit()
    
    
def get_user_by_id(id):
    cur.execute('SELECT * FROM users WHERE id=?', [id])
    return cur.fetchone() # (1, 'Булат', 'admin@admin', 'qwerty')


def get_user_by_email(email):
    cur.execute(f'SELECT * FROM users WHERE email="{email}"')
    return cur.fetchone() # (1, 'Булат', 'admin@admin', 'qwerty')