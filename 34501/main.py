import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT
    )''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER,
    email TEXT,
    phone TEXT
    )''')
conn.commit()


# Добавление
# cur.execute('INSERT INTO products(name, price, description) VALUES (?,?,?)', ['Гитара Электро', 50000, 'Крутая электро гитара'])
# conn.commit()

#Удаление
# cur.execute('DELETE FROM products WHERE id=?', [2])
# conn.commit()

#Получить
# cur.execute('SELECT * FROM products')
# result = cur.fetchall()
# for item in result:
#     for i in item:
#         print(i)
#     print('_'*20)

name = input('Введите название товара: ')
cur.execute('SELECT * from products where name=?', [name])
result = cur.fetchall()
print(result)