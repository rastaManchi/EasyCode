import sqlite3


conn = sqlite3.connect('mydb.db', check_same_thread=False)
cur = conn.cursor()


cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            username TEXT,
            first_name TEXT,
            surname TEXT,
            is_admin INTEGER DEFAULT 0,
            phone TEXT
        )
            ''')
conn.commit()

# 1. TODO: Создать таблицу tickets (id, name, phone, user_id)


def add_user(user_id: str, 
             username: str,
             first_name: str,
             surname: str, 
             phone: str) -> bool:
    cur.execute(f'SELECT * FROM users WHERE user_id={user_id}')
    user = cur.fetchone() # (1, 'username', 'Имя', 'Фамилия', ...)
    if not user:
        cur.execute('''INSERT INTO users
                    (user_id, username, first_name, surname, phone)
                    VALUES 
                    (?, ?, ?, ?, ?)
                    ''', [user_id, username, first_name, surname, phone])
        conn.commit()
        return True
    return False

# 2. TODO: Создать функцию добавления билета add_ticket
