import sqlite3


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
        FOREIGN KEY (user_id) REFERENCES users(id)
    )        
            ''')
conn.commit()


def get_all_posts():
    cur.execute('SELECT * FROM posts')
    return cur.fetchall() # [ (1, 'Название', 'Контент'),  (2, 'Название', 'Контент') ]


def get_posts_by_user_id(user_id):
    cur.execute(f'''SELECT * FROM posts
                    WHERE user_id={user_id}''')
    return cur.fetchall()


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
    cur.execute(f'SELECT * FROM users WHERE id={id}')
    return cur.fetchone() # (1, 'Булат', '@mail.ru', '123')