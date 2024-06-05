import matplotlib.pyplot as plt
import sqlite3
import time

conn = sqlite3.connect('registros.db')
cursor = conn.cursor()


def usuario(id,nombrecompleto):
    plt.figure(figsize=(19, 10), dpi=100)
    cursor.execute("""
        SELECT strftime('%Y-%m', datetime(timecreated, 'unixepoch')) AS mes,
               COUNT(*) AS count
        FROM registros
        WHERE userid = """+str(id)+"""
        GROUP BY mes
        ORDER BY mes
    """)

    results = cursor.fetchall()

    x = []  
    y = []  

    for row in results:
        x.append(row[0])
        y.append(row[1])
        print(str(row[0])+" - "+str(row[1]))
       

    plt.bar(x, y)

    plt.xlabel('Mes')
    plt.ylabel('Número de visitas')
    plt.title('Visitas por mes: '+nombrecompleto)

    plt.xticks(rotation=45)

    
    plt.savefig(str(id)+" - "+nombrecompleto+".png")
    
cursor.execute("""
        SELECT
        id,firstname,lastname
        FROM usuarios
    """)

resultados = cursor.fetchall()

for linea in resultados:
    print("usuario:|||||||||||||||||")
    nombre = ""
    apellido = ""
    if linea[1] is not None:
        nombre = linea[1]
    if linea[2] is not None:
        apellido = linea[2]
    print(linea[0])
    print(linea[1])
    print(linea[2])
    
    try:
        
        usuario(linea[0],nombre+" "+apellido)
    except Exception as e:
        print(e)
    time.sleep(1)
conn.close()
