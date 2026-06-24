import sqlite3 

conn = sqlite3.connect('clients.db')
cur = conn.cursor() 

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    numberPhone INTEGER UNIQUE,
    room INTEGER,    
    diagnosis TEXT  
)
 ''')
conn.commit()

cur.execute('''INSERT OR IGNORE INTO users (name, age, numberPhone, room, diagnosis) VALUES (?, ?, ?, ?, ?)''', ['Павел', 16, 89001009090, 1, 'простуда'])
conn.commit()

users_data = [
    ('Владимир', 16, 89001009091, 2, 'простуда'),
    ('Анна', 17, 89001009092, 3, 'простуда'),
    ('Виктор', 15, 89001009093, 4, 'простуда')
]
cur.executemany('''
INSERT OR IGNORE INTO users (name, age, numberPhone, room, diagnosis)
VALUES (?, ?, ?, ?, ?)''', users_data)
conn.commit()

cur.execute('SELECT * FROM users')
all_users = cur.fetchall()
print(all_users)

cur.execute('SELECT * FROM users WHERE age > 16')
one_users = cur.fetchall()
print(one_users)

#cur.execute('UPDATE users SET diagnosis = ? WHERE name = ?', ['простуда','Виктор'])
#conn.commit()

cur.execute(f'DELETE FROM users WHERE age > {16}')
conn.commit()