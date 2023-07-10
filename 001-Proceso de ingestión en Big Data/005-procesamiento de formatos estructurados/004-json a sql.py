import sqlite3
import json

with open('clientes.json') as f:
    data = json.load(f)

conexion = sqlite3.connect('basedatos.db')
cursor = conexion.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id text, nombre text, edad text,email text)')

for registro in data:
    cursor.execute('INSERT INTO clientes VALUES (?, ?, ?,?)', (registro['id'], registro['nombre'], registro['edad'],registro['email']))

conexion.commit()
conexion.close()
