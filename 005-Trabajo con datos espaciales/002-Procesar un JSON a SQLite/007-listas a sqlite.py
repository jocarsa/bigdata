import csv
import ast
import json
import sqlite3

filename = 'registros.csv'

conn = sqlite3.connect('registros.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros (
        epoch INTEGER,
        jugador TEXT,
        px INTEGER,
        py INTEGER
    )
''')

with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter='|')
    line_count = 0
    
    for row in csv_reader:
       
        try:
            fecha = row[0]
            
            datos = row[1]
            lista = ast.literal_eval(datos)
            mifecha = []
            nombre = []
            px = []
            py = []
            
            #print(lista)
            for elemento in lista:
                try:
                    mifecha = fecha
                    nombre = elemento['name']
                    px = elemento['px']
                    py = elemento['py']
                    cursor.execute('''
                        INSERT INTO registros (epoch, jugador, px, py)
                        VALUES (?, ?, ?, ?)
                    ''', (mifecha, nombre, px, py))
                except:
                    pass
        except:
            pass
            
        
        
        line_count += 1
# Commit the changes
conn.commit()

# Close the connection
conn.close()
