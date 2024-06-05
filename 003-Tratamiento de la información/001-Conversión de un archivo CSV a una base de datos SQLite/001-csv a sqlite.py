import pandas as pd
import sqlite3

datos = pd.read_csv('registros.csv')

conexion = sqlite3.connect('registros.db')
datos.to_sql('registros', conexion, if_exists='replace', index=True)
conexion.close()
