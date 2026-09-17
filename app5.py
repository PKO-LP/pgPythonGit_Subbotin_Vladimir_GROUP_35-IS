import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="Admin"
)
cur = conn.cursor()
cur.execute("SELECT Название, Год FROM tracks WHERE Год > 2015;")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()