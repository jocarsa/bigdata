import sqlite3

connection = sqlite3.connect('empresas.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM empresas')

for row in cursor:
    print(row)

cursor.close()
connection.close()
