import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('registros.db')

cursor = conn.cursor()

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

''')
data = cursor.fetchall()

x = [row[0] for row in data]
y = [row[1] for row in data]

plt.scatter(x, y)

plt.title('Scatter Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

conn.close()
