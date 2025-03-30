import sqlite3

conn = sqlite3.connect('27276/sql.db')
cur = conn.cursor()

# Создать таблицу
# cur.execute('''CREATE TABLE products(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             price INTEGER,
#             description TEXT)''')
# conn.commit()

# Добавить данные
# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['Название1', 1, 'Описание1'])
# conn.commit()

# Достать данные
# cur.execute('SELECT * FROM products')
# result = cur.fetchall()
# print(result)

# Удаление данных
# cur.execute('DELETE FROM products WHERE name = ?', ['Название1'])
# conn.commit()


# cur.execute('SELECT name, price FROM products WHERE price < ?', [100])
# result = cur.fetchall()
# print(result)