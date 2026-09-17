import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="Admin"
)
cur = conn.cursor()

cur.execute("SELECT * FROM tracks WHERE Исполнитель = 'Linkin Park';")

rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()