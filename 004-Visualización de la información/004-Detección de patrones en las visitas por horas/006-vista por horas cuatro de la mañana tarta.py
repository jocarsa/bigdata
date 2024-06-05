import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT 
strftime('%H', datetime(utc, 'unixepoch')) AS hora,
COUNT(Identificador) as Numero,
usuario
           
FROM registros
WHERE hora LIKE '%04%'
GROUP BY usuario
ORDER BY Numero DESC
""")

results = cursor.fetchall()

x = []  
y = []  

for row in results:
    x.append(row[1])
    y.append(row[2])
    print(str(row[0])+" - "+str(row[1]))
   

plt.pie(x, labels=y)


plt.title('Visitas por hora')

plt.xticks(rotation=45)

conn.close()
plt.show()
