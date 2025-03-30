import sqlite3


conn = sqlite3.connect('27927/music.db')
cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS products(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             price INTEGER,
#             description TEXT
#             )''')
# conn.commit()


# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['Название4', 300, 'image.png'])
# conn.commit()

cur.execute('DELETE FROM products WHERE id>1 and id<10')
conn.commit()

# cur.execute('SELECT * FROM products')
# result = cur.fetchmany(2)
# print(result)
# print(cur.fetchone())
# print(cur.fetchone())

name = input('Введите название товара: ')
cur.execute('SELECT * FROM products')
result = cur.fetchall()

for item in result:
    if item[1] == name:
        print(f'Название: {item[1]}\nОписание: {item[3]}\nЦена: {item[2]}')