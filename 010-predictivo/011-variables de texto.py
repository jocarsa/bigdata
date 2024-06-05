import pandas as pd
import sqlite3
from collections import Counter
import matplotlib.pyplot as plt
import tkinter as tk


def calcula(minota1,minota2):
    plt.figure(figsize=(8, 8), dpi=100)
    conexion = sqlite3.connect('notas.db')

    cursor = conexion.cursor()
    nota1 = minota1

    cursor.execute("""
        SELECT * FROM notas
        WHERE FK_Evaluacion_Evaluacion = '1'
        AND
        Nota = '"""+str(nota1)+"""'
        """)

    resultado = cursor.fetchall()

    nota2 = minota2

    cursor.execute("""
        SELECT * FROM notas
        WHERE FK_Evaluacion_Evaluacion = '2'
        AND
        Nota = '"""+str(nota2)+"""'
        """)
    listadenotas = []

    resultado2 = cursor.fetchall()
    coincidencias = 0
    for registro in resultado:
        for registro2 in resultado2:
            if registro[3] == registro2[3] and registro[4] == registro2[4]:
                coincidencias += 1
                cursor.execute("""
                SELECT * FROM notas
                WHERE FK_Evaluacion_Evaluacion = '3'
                AND
                FK_Modulos_Nombre = '"""+registro[4]+"""'
                AND
                FK_Alumnos_Apellidos_Nombre = '"""+registro[3]+"""'
                """)
                resultado3 = cursor.fetchall()
                if len(resultado3) != 0:
                    #print(resultado3)
                    if resultado3[0][6] <= 10:
                        listadenotas.append(resultado3[0][6])

    print(listadenotas)
    print(coincidencias)


    counter = Counter(listadenotas)
    total_count = len(listadenotas)

    labels = counter.keys()
    sizes = counter.values()

    for number, count in counter.items():
        percent = (count / total_count) * 100
        print(f"{number}: {percent}%")

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

#calcula(7,8)

def calculame():
    v1 = var1.get()
    v2 = var2.get()
    calcula(v1,v2)  

raiz = tk.Tk()
marco = tk.Frame(raiz)
marco.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Label(marco,text="Introduce la nota en primera evaluación").pack()
entrada1 = tk.Entry(marco,textvariable=var1)
entrada1.pack()
tk.Label(marco,text="Introduce la nota en segunda evaluación").pack()
entrada2 = tk.Entry(marco,textvariable=var2)
entrada2.pack()
tk.Button(text="Envía consulta",command=calculame).pack()
raiz.mainloop()









