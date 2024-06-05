import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT strftime('%H', datetime(utc, 'unixepoch')) AS hora,
           COUNT(*) AS count
    FROM registros
    WHERE hora IS NOT NULL
    GROUP BY hora
    ORDER BY hora
""")

results = cursor.fetchall()

x = []  
y = []  

for row in results:
    x.append(row[0])
    y.append(row[1])
    print(str(row[0])+" - "+str(row[1]))
   

plt.bar(x, y)

plt.xlabel('Hora')
plt.ylabel('Número de visitas')
plt.title('Visitas por hora')

plt.xticks(rotation=45)

conn.close()
plt.show()
