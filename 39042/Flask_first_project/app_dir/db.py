import sqlite3


db = sqlite3.connect('database.db', check_same_thread=False)
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
)''')
db.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            author INT
)''')
db.commit()


def add_new_post(title, content, author_id):
    cur.execute('INSERT INTO posts(title, content, author) VALUES (?, ?, ?)', [title, content, author_id])
    db.commit()
    

def get_all_posts():
    cur.execute('SELECT * FROM posts')
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
    cur.execute("""SELECT * FROM posts WHERE title LIKE
                :keyword OR content LIKE
                :keyword""", {'keyword': f'%{text}%'})
    return cur.fetchall() # [ (1, title, content, author),  ]


# SELECT * FROM ITEMS WHERE Country LIKE '%я_'

