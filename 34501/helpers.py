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

cur.execute('''CREATE TABLE IF NOT EXISTS slides(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    len INTEGER,
    description TEXT
    )''')
conn.commit()

def get_all_slides():
    cur.execute('SELECT * FROM slides')
    return cur.fetchall()

cur.execute('INSERT INTO slides(name, len, description) VALUES (?,?,?)', ['Детская', 5, 'На этой горке можно оставить детей, пока вы сами получаете адреналин на одной из взрослых горок.'])
conn.commit()

cur.execute('INSERT INTO slides(name, len, description) VALUES (?,?,?)', ['Закатное солнце', 20, 'Одна из самых популярных горок, Можно кататься как взрослым, так и детям от шести лет.'])
conn.commit()

cur.execute('INSERT INTO slides(name, len, description) VALUES (?,?,?)', ['Жираф', 31, 'На этой горке можно испытать те же чувства, что и при скатывании по шее настоящего жирафа. Одна из самых популярных горок.'])
conn.commit()

cur.execute('INSERT INTO slides(name, len, description) VALUES (?,?,?)', ['Красный дракон', 53, 'Горка в японском стиле. В верхней части тоннеля горки расположено несколько мониторов, на которых можно посмотреть аниме.'])
conn.commit()

cur.execute('INSERT INTO slides(name, len, description) VALUES (?,?,?)', ['Кантемир', 100, 'Не самая популярная горка, потому что не все любят экстрим. Если вы хотите провести ближайший час незабываемо, эта длинная горка - для вас.'])
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


