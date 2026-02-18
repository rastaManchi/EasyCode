import sqlite3


conn = sqlite3.connect('test.db')
cur = conn.cursor()


cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
            ''')
conn.commit()


# cur.execute('INSERT INTO users(username, email) VALUES (?, ?)', ['Илан', '213mail.ru'])
# conn.commit()


# cur.execute("SELECT username, email FROM users")
# cur.execute("SELECT * FROM users")
cur.execute("SELECT * FROM users WHERE id>1")
print(cur.fetchall())