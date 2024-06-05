import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT strftime('%Y-%m', datetime(utc, 'unixepoch')) AS mes,
           COUNT(*) AS count
    FROM registros
    WHERE
    (
    mes LIKE '%2021%'
    OR
    mes LIKE '%2022%'
    OR
    mes LIKE '%2023%'
    )
    GROUP BY mes
    ORDER BY mes
""")

results = cursor.fetchall()

x = []  
y = []  

for row in results:
    x.append(row[0])
    y.append(row[1])
   

plt.plot(x, y)

plt.xlabel('Mes')
plt.ylabel('Número de visitas')
plt.title('Visitas por mes')

plt.xticks(rotation=45)

conn.close()
plt.show()
