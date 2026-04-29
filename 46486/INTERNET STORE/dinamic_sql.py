import sqlite3

# conn = sqlite3.connect()
# cur = conn.cur()

is_id = False
is_expires_at = True
is_order_by = True
sql = 'SELECT * FROM posts WHERE'
params = []
conditions = []


if is_id:
    conditions.append('id=?')
    params.extend([1])
if is_expires_at:
    conditions.append('expires_at=?')
    params.extend([2])
sql += ' AND '.join(conditions)
if is_order_by:
    sql += 'ORDER BY ?'
    params.extend(['id'])

print(sql, params)
# cur.execute(sql, params)