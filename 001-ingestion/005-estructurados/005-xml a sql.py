import xml.etree.ElementTree as ET
import sqlite3

# Analizar el archivo XML
tree = ET.parse('clientes.xml')
root = tree.getroot()

# Conectar a la base de datos SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Crear la tabla en la base de datos
cursor.execute('''CREATE TABLE IF NOT EXISTS items
                  (id INTEGER PRIMARY KEY,
                   nombre TEXT,
                   edad INTEGER,
                   email TEXT)''')

# Insertar los datos en la tabla
for item in root.findall('item'):
    id = item.find('id').text
    nombre = item.find('nombre').text
    edad = item.find('edad').text
    email = item.find('email').text
    
    cursor.execute('''INSERT INTO items (id, nombre, edad, email)
                      VALUES (?, ?, ?, ?)''', (id, nombre, edad, email))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
