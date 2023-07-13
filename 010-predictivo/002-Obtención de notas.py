import pandas as pd
import sqlite3

conexion = sqlite3.connect('notas.db')

cursor = conexion.cursor()
nota1 = input("Introduce la nota del alumno en la primera evaluación:")

print("La nota que has introducido es: "+str(nota1))

cursor.execute("""
    SELECT * FROM notas
    WHERE FK_Evaluacion_Evaluacion = '1'
    AND
    Nota = '"""+nota1+"""'
    """)

resultado = cursor.fetchall()
print(resultado)
