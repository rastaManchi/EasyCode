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

def add_product():
    cur.execute('INSERT INTO products(name, price, description) VALUES (?,?,?)', ['Скрипка', 100000000, 'Старинная скрипка'])
    conn.commit()

def select_product():
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()
    print(products)

