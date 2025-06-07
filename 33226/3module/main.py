import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            description TEXT
            )''')
conn.commit()


# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['Гитара', 1000, '...'])
# conn.commit()


# def delete_item_by_name(name):
#     cur.execute('DELETE FROM products WHERE name=? ', [name])
#     conn.commit()


# cur.execute('SELECT * FROM products WHERE price<?', [10001])
# result = cur.fetchall()


def second():
    cur.execute('SELECT price FROM products')
    result = cur.fetchall()
    price_count = 0
    total = 0
    for i in result:
        total += i[0]
        price_count += 1
    print(total/price_count)

second()
