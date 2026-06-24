import sqlite3 

conn = sqlite3.connect('blog.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE NOT NULL,
            password TEXT
            )
''')

cur.execute('''CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            user_id INTEGER,
            category_id INTEGER,
            created_ad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
            )''')
conn.commit()

default_categories = [
    ('Программирование','Статьи о программировании и разработке'),
    ('Дизайн', 'Статьи о дизайне и UX/UI'),
    ('Путешествия', 'Статьи о путешествиях'),
    ('Кулинария','Рецепты и кулинарные советы'),
    ('Спорт', ' Новости и статьи о спорте')
]

for category in default_categories:
    cur.execute('INSERT OR IGNORE INTO categories(name, description) VALUES (?,?)', category)

def add_user(name,email,password):
    cur.execute('''INSERT OR IGNORE INTO users (name, email, password) VALUES (?, ?, ?)''',[name, email, password])
    conn.commit()

def get_user_by_id(id):
    cur.execute('SELECT * FROM users WHERE id=?',[id])
    return cur.fetchone()

def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email=?',[email])
    return cur.fetchone()

def new_post(title,content,user_id,category_id):
    cur.execute('''INSERT OR IGNORE INTO posts (title,content,user_id,category_id) VALUES (?,?,?,?)''',[title,content,user_id,category_id])
    conn.commit()

def get_all_post():
    cur.execute('SELECT * FROM posts')
    return cur.fetchall()

def get_posts_by_user(user_id):
    cur.execute('SELECT * FROM posts WHERE user_id = ?', [user_id])
    return cur.fetchall()

def get_all_users():
    cur.execute('SELECT * FROM  users')
    return cur.fetchall()

def get_all_categories():
    cur.execute('SELECT * FROM categories')
    return cur.fetchall()

def get_posts_by_category(category_id):
    cur.execute('''SELECT posts.*, users.name, categories.name as category_name
                FROM posts
                JOIN users ON posts.user_id = users.id
                LEFT JOIN categories ON posts.category_id = categories.id
                WHERE posts.category_id = ?
                ORDER BY posts.created_at DESC ''',
            [category_id])
    return cur.fetchall()

def search_posts(query):
    search_pattern = f'%{query}%'
    cur.execute('''SELECT posts.*, users.name, categories.name as category_name
                FROM posts
                JOIN users ON posts.user_id = users.id
                LEFT JOIN categories ON posts.category_id = categories.id
                WHERE posts.title LIKE ? OR posts.content LIKE ? ''',
                [search_pattern, search_pattern])
    return cur.fetchall()