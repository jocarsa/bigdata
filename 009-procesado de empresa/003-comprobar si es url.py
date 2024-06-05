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

cursor.execute('SELECT * FROM empresas')

for row in cursor:
    if is_valid_url(row[1]):
        print("valido")
    else:
        print("no valido")

cursor.close()
connection.close()
