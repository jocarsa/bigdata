import csv
import ast

filename = 'registros.csv'

with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter='|')
    line_count = 0
    
    for row in csv_reader:
        if line_count >= 10:
            break
        
        fecha = row[0]
        print("La fecha es: "+fecha)
        datos = row[1]
        lista = ast.literal_eval(datos)
        print("Los datos son: ")
        print(lista)
        for elemento in lista:
            
        
        
        line_count += 1
