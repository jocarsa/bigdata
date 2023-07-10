import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('registros.db')

cursor = conn.cursor()

cursor.execute('''
SELECT jugador
FROM registros
GROUP BY jugador

''')

jugadores = cursor.fetchall()

for jugador in jugadores:
    plt.figure(figsize=(19, 10), dpi=100)

    cursor.execute('''
    SELECT
    px,
    py
    FROM registros
    WHERE
    px != 200
    AND
    py != 200
    AND px IS NOT NULL
    AND py IS NOT NULL
    AND px != ''
    AND py != ''
    AND jugador = "'''+jugador[0]+'''"

    ''')
    data = cursor.fetchall()

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.scatter(x, y)

    plt.title(jugador[0])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.savefig(jugador[0]+".png")

conn.close()
