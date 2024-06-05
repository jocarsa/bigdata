import sqlite3
import re
from urllib.parse import urlparse

def url_contains_forbidden_term(url, forbidden_terms):
    for term in forbidden_terms:
        if re.search(term, url, re.IGNORECASE):
            return True
    return False

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
exclusion = ['cincodias','infocif','google','einforma','expansion','eleconomista','axesor','linkedin','iberinform','boe','datoscif','administracion','cnmv']
connection = sqlite3.connect('empresas.db')
connection2 = sqlite3.connect('empresas.db')
cursor = connection.cursor()
cursor2 = connection2.cursor()
cursor.execute('SELECT * FROM empresas')

for row in cursor:
    if is_valid_url(row[1]):     
        if url_contains_forbidden_term(row[1], exclusion):
            print("excluido")
        else:
            archivo = open("empresas.csv",'a')
            archivo.write(row[0]+","+row[1]+"\n")
            print("valido")
    else:
        print("no valido")
             
archivo.close()
cursor.close()
connection.close()
