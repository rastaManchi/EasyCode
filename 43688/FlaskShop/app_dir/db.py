import sqlite3


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


def add_user(name, email, password):
    cur.execute('''
        INSERT INTO users(name, email, password) VALUES
        (?, ?, ?)
                ''', [name, email, password])
    conn.commit()
    

def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email=?', [email])
    return cur.fetchone() # (1, 'Булат', '@mail.ru', '123')


def get_user_by_id(id):
    cur.execute(f'SELECT * FROM users WHERE id={id}')
    return cur.fetchone() # (1, 'Булат', '@mail.ru', '123')