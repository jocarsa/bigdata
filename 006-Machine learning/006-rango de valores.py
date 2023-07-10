import matplotlib.pyplot as plt
import sqlite3

def check_odd_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

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

diadelasemana = [247,936,960,1053,834,681,201]

x = []  
y = []  
colors = []
for row in results:
    x.append(row[0])
    y.append(row[2])
    print("el valor de hoy es :"+str(row[2]))
    print("valor medio es de: "+str(diadelasemana[int(row[1])]))
    if (row[2] - diadelasemana[int(row[1])]) > 500:
        colors.append("red")
    elif (row[2] - diadelasemana[int(row[1])]) < -500:
        colors.append("blue")
    else:
        colors.append("green")
    print(str(row[0])+" - "+str(row[1]))
   

plt.bar(x, y, color=colors)

plt.xlabel('Mes')
plt.ylabel('Número de visitas')
plt.title('Visitas por día')

plt.xticks(rotation=45)

conn.close()
plt.show()
