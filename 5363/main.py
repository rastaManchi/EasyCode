import sqlite3


conn = sqlite3.connect('new.db')
cur = conn.cursor()

# SELECT, INSERT, UPDATE, DELETE

cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        url TEXT
            )
''')

conn.commit()


def add_product():
    cur.execute('INSERT INTO products (name, price, url) VALUES (?, ?, ?)', ['RTX6090', 10010.50, 'https://buy.ru/1'])
    conn.commit()

def select_product():
    cur.execute('SELECT * FROM products')
    result = cur.fetchall()
    print(result)

def update_product():
    cur.execute('UPDATE products SET price = 100 WHERE id = 1')
    conn.commit()

def delete_product():
    cur.execute('DELETE FROM products WHERE id = 1')
    conn.commit()
