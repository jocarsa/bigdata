import csv
import ast
import json

filename = 'registros.csv'

with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter='|')
    line_count = 0
    
    for row in csv_reader:
       
        try:
            fecha = row[0]
            
            datos = row[1]
            lista = ast.literal_eval(datos)
            mifecha = []
            nombre = []
            px = []
            py = []
            
            #print(lista)
            for elemento in lista:
                try:
                    mifecha = fecha
                    nombre = elemento['name']
                    px = elemento['px']
                    py = elemento['py']
                except:
                    print("algun error")
        except:
            print("linea no legible")
            
        
        
        line_count += 1
