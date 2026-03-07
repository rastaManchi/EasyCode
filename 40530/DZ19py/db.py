import sqlite3
conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            is_admin integer default 0
)
''')
conn.commit()

def add_admin(id):
    cur.execute(f'''update users set is_admin = 1 
                where id = {id}''')
    conn.commit()

def is_admin(id):
    cur.execute('SELECT is_admin FROM users WHERE id=?', [id])
    is_admin = cur.fetchone()
    print(is_admin)
    if is_admin[0]:
        return True
    return False    

add_admin(1)

cur.execute('''
CREATE TABLE IF NOT EXISTS posts(
            id_posts INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            status integer default 0
)
''')
conn.commit()


cur.execute('''
CREATE TABLE IF NOT EXISTS tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
)
''')
conn.commit()


def check_token(token):
    cur.execute('SELECT * FROM tokens WHERE token=?', [token])
    return cur.fetchone()


def create_token(user_id, token):
    cur.execute('INSERT INTO tokens (token, user_id) VALUES (?, ?)', [token, user_id])
    conn.commit()


def add_user(name, email, password):
    cur.execute('INSERT INTO users(name, email, password) VALUES (?, ?, ?)', [name, email, password])
    conn.commit()


def get_user_by_id(user_id):
    cur.execute(f'SELECT * FROM users WHERE id = {user_id}')
    return cur.fetchone() # (1, 'Булат', 'admin@admin.ru', 'qwerty')


def get_user_by_email(user_email):
    cur.execute('SELECT * FROM users WHERE email=?', [user_email])
    return cur.fetchall() # [(1, 'Булат', 'admin@admin.ru', 'qwerty')]




def add_post_in_db(title, content):
    cur.execute('INSERT INTO posts(title, content) VALUES (?, ?)', [title, content])
    conn.commit()

def get_posts():
    cur.execute('''SELECT * FROM posts
                where status = 1''')
    return cur.fetchall()

def search_post(text):
    cur.execute("""SELECT * FROM posts WHERE (title LIKE
                :keyword OR content LIKE
                :keyword)""", {'keyword': f'%{text}%'})
    return cur.fetchall()

def search_zero_posts():
    cur.execute("""SELECT * FROM posts
                WHERE status = 0
""")
    return cur.fetchall()


def status_post_approve(id_post):
    cur.execute(f"""update posts set status = 1
                where id_posts = {id_post}""")
    conn.commit()

def status_post_disapprove(id_post):
    cur.execute(f"""update posts set status = 2
                where id_posts = {id_post}""")
    conn.commit()
