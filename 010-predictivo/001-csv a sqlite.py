import pandas as pd
import sqlite3

datos = pd.read_csv('notas.csv')

conexion = sqlite3.connect('notas.db')
datos.to_sql('notas', conexion, if_exists='replace', index=True)
conexion.close()
