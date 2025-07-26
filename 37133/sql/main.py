import sqlite3

conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT
    )''')
conn.commit()


# cur.execute('INSERT INTO products(name, price, description) VALUES (?, ?, ?)', ['Гитара', 7500, 'Крутая гитара'])
# conn.commit()