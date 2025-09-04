import sqlite3
conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER,
            Admin INTEGER,
            Userid TEXT
            ) ''')
conn.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS questions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            answer1 TEXT,
            answer2 TEXT,
            answer3 TEXT,
            answer4 TEXT,
            correct TEXT
            )''')
conn.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS gamestate(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gamestate TEXT
            )''')
conn.commit()


# cur.execute("INSERT INTO gamestate(gamestate) VALUES ('OFF')")
# conn.commit()


def useradd(Userid):
    cur.execute('INSERT INTO user(score, Admin, Userid) VALUES (?,?,?)', [0,0,Userid])
    conn.commit()

def userget(userid):
    cur.execute('SELECT * FROM user WHERE Userid = ?', [userid])
    r = cur.fetchone()
    return r

def addadmin(addadmin):
    cur.execute('UPDATE user SET Admin= 1 WHERE Userid = ?', [addadmin])
    conn.commit()

def db_startgame():
    cur.execute("UPDATE gamestate SET gamestate='ON'")
    conn.commit()

def db_stopgame():
    cur.execute("UPDATE gamestate SET gamestate='OFF'")
    conn.commit()

def add_question(text, v1, v2, v3, v4, correct):
    cur.execute("INSERT INTO questions(text, answer1, answer2, answer3, answer4, correct) VALUES (?, ?, ?, ?, ?, ?)", [text, v1, v2, v3, v4, correct])
    conn.commit()

def delete_all_questions():
    cur.execute("DELETE FROM questions")
    conn.commit()

def get_question(index):
    cur.execute("SELECT * FROM questions")
    result = cur.fetchall()
    return result[index]