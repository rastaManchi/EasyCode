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


# cur.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', ['Кларнет', 5000000, 'зычковый деревянный духовой музыкальный инструмент с одинарной тростью. Был изобретён примерно в 1700-х в Нюрнберге, в музыке активно используется со второй половины XVIII века.'])
# conn.commit()


cur.execute('SELECT * FROM products')
result = cur.fetchall()

print(result)

