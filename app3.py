import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="Admin"
)

cur = conn.cursor()

cur.execute("SELECT Название, Исполнитель, Год FROM tracks;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()