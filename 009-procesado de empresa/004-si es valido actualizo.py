import sqlite3
import re
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

connection = sqlite3.connect('empresas.db')
cursor = connection.cursor()
cursor2 = connection.cursor()
cursor.execute('SELECT * FROM empresas')

for row in cursor:
    if is_valid_url(row[1]):
        cursor2.execute('''
            UPDATE empresas SET webok = "'''+row[1]+'''"
            WHERE Empresa = "'''+row[0]+'''"

            ''')
        connection.commit()
        print("valido")
    else:
        print("no valido")
        cursor2.execute('''
        UPDATE empresas SET webok = ""
WHERE Empresa = "'''+row[0]+'''"

''')
        connection.commit()
        

cursor.close()
connection.close()
