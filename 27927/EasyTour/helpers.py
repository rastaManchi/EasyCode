import sqlite3
import json

conn = sqlite3.connect('EasyTour/tours.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS tours(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price INTEGER,
        category TEXT, 
        country TEXT,
        days INTEGER
            )
''')
conn.commit()

# file = open('27927/EasyTour/tours_info.json', 'r', encoding='utf-8')
# data = json.loads(file.read())

# for tour in data:
#     payload = [tour['name'],
#                tour['description'],
#                tour['price'],
#                tour['category'],
#                tour['country'],
#                tour['days']]
#     cur.execute('INSERT INTO tours (name, description, price, category, country, days) VALUES (?, ?, ?, ?, ?, ?)', payload)
#     conn.commit()


def get_all_tours():
    cur.execute('SELECT * FROM tours')
    return cur.fetchall()



