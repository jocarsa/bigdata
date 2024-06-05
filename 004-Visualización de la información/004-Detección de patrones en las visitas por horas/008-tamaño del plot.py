import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()
for hora in range(0,24):
    plt.figure(figsize=(19, 10), dpi=100)  # Width = 800 pixels, Height = 600 pixels, DPI = 100
    cursor.execute("""
        SELECT 
    strftime('%H', datetime(utc, 'unixepoch')) AS hora,
    COUNT(Identificador) as Numero,
    usuario
               
    FROM registros
    WHERE hora LIKE '%"""+str(hora).zfill(2)+"""%'
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


    plt.title('Visitas por hora: '+str(hora))

    

    plt.savefig("Visitas por hora - "+str(hora)+".png")

conn.close()
