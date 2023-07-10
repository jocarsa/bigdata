import csv

filename = 'registros.csv'

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    line_count = 0
    
    for row in csv_reader:
        if line_count >= 10:
            break
        
        # Process the row data
        print(row)
        
        line_count += 1
