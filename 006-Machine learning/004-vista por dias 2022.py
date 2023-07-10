import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT strftime('%Y-%m-%d', datetime(utc, 'unixepoch')) AS dia,
        strftime('%w', datetime(utc, 'unixepoch')) AS weekday,
           COUNT(*) AS count
    FROM registros
    WHERE
    (

    dia LIKE '%2022%'

    )
    GROUP BY dia
    ORDER BY dia
""")

results = cursor.fetchall()

diadelasemana = [8538,26007,25679,30750,23741,19170,6184]

x = []  
y = []  
colors = []
for row in results:
    x.append(row[0])
    y.append(row[2])
    colors.append("red")
    print(str(row[0])+" - "+str(row[1]))
   

plt.bar(x, y, color=colors)

plt.xlabel('Mes')
plt.ylabel('Número de visitas')
plt.title('Visitas por día')

plt.xticks(rotation=45)

conn.close()
plt.show()
