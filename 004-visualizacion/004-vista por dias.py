import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT strftime('%Y-%m-%d', datetime(utc, 'unixepoch')) AS dia,
           COUNT(*) AS count
    FROM registros
    WHERE
    (
    dia LIKE '%2021%'
    OR
    dia LIKE '%2022%'
    OR
    dia LIKE '%2023%'
    )
    GROUP BY dia
    ORDER BY dia
""")

results = cursor.fetchall()

x = []  
y = []  

for row in results:
    x.append(row[0])
    y.append(row[1])
    print(str(row[0])+" - "+str(row[1]))
   

plt.plot(x, y)

plt.xlabel('Mes')
plt.ylabel('Número de visitas')
plt.title('Visitas por mes')

plt.xticks(rotation=45)

conn.close()
plt.show()
