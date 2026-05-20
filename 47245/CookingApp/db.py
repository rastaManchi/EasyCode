import sqlite3


conn = sqlite3.connect('recipes.db', check_same_thread=False)
cur = conn.cursor()


cur.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                ingredients TEXT,
                steps TEXT
            )
        """)
conn.commit()
