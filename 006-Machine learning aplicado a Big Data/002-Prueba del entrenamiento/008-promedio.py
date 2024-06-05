import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute("""
  SELECT strftime('%w', datetime(utc, 'unixepoch')) AS weekday, 
       COUNT(*) / COUNT(DISTINCT DATE(utc, 'unixepoch')) AS average_entries
FROM registros
GROUP BY weekday;
""")

results = cursor.fetchall()

x = []  
y = []
diadelasemana = []

for row in results:
    x.append(row[0])
    y.append(row[1])
    diadelasemana.append(row[1])
    print(str(row[0])+" - "+str(row[1]))
   
print(diadelasemana)
plt.bar(x, y)

plt.xlabel('Mes')
plt.ylabel('Número de visitas')
plt.title('Visitas por mes')

plt.xticks(rotation=45)



conn.close()
plt.show()
