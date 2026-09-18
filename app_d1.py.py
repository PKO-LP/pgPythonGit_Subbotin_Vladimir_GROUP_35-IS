import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_bd",
    user="postgres",
    password="Admin"
)

cur = conn.cursor()

nazvanie = input("Название: ")
ispolnitel = input("Исполнитель: ")
god = int(input("Год: "))
dlitelnost = int(input("Длительность (сек): "))

cur.execute(
    "INSERT INTO tracks (Название, Исполнитель, Год, Длительность) VALUES (%s, %s, %s, %s);",
    (nazvanie, ispolnitel, god, dlitelnost)
)
conn.commit()

cur.execute("SELECT * FROM tracks;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()