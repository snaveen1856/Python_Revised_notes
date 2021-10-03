import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

m = cursor.execute("""
SELECT * FROM mark_employee
""")

for x in m:
    print(x[0], x[0])

conn.commit()
cursor.close()
conn.close()
