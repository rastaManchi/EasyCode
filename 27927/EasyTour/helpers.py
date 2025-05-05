import sqlite3

conn = sqlite3.connect('tours.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tours(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price INTEGER,
            category TEXT,
            country TEXT,
            days INTEGER,
            likes INTEGER
)''')
conn.commit()

def get_all_tours():
    cur.execute('SELECT * FROM tours')
    return cur.fetchall()


def get_tour_covers():
    cur.execute('SELECT id, name FROM tours')
    return cur.fetchall()

def get_cover_by_id(tour_id):
    cur.execute(f'SELECT id, name FROM tours WHERE id = {tour_id}')
    return cur.fetchone()

def get_tours_with_keywords(minprice, maxprice, keyword):
    cur.execute(f"""SELECT * FROM tours WHERE name LIKE 
                :keyword OR description LIKE 
                :keyword OR country LIKE 
                :keyword AND price <= {maxprice} AND price >= {minprice}"""
                , {'keyword': f'%{keyword}%'})
    return cur.fetchall()
    
def get_tours_by_category(category):
    cur.execute(f'SELECT * FROM tours WHERE category LIKE :categ', {'categ': f'%{category}%'})
    return cur.fetchall()

def get_tour_by_id(tour_id):
    cur.execute(f'SELECT * FROM tours WHERE id = {tour_id}')
    return cur.fetchone()


def add_like(tour_id):
    cur.execute(f"SELECT likes FROM tours WHERE id = {tour_id}")
    likes = cur.fetchone()[0]
    if not likes:
        likes = 0
    likes += 1
    cur.execute(f"UPDATE tours SET likes = {likes} WHERE id = {tour_id}")
    conn.commit()
