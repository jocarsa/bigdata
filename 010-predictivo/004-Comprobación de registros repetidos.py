import pandas as pd
import sqlite3

conexion = sqlite3.connect('notas.db')

cursor = conexion.cursor()
nota1 = input("Introduce la nota del alumno en la primera evaluación: ")

cursor.execute("""
    SELECT * FROM notas
    WHERE FK_Evaluacion_Evaluacion = '1'
    AND
    Nota = '"""+nota1+"""'
    """)

resultado = cursor.fetchall()

nota2 = input("Introduce la nota del alumno en la segunda evaluación: ")

cursor.execute("""
    SELECT * FROM notas
    WHERE FK_Evaluacion_Evaluacion = '2'
    AND
    Nota = '"""+nota2+"""'
    """)

resultado2 = cursor.fetchall()
coincidencias = 0
for registro in resultado:
    for registro2 in resultado2:
        if registro[3] == registro2[3] and registro[4] == registro2[4]:
            coincidencias += 1
            

print(coincidencias)












