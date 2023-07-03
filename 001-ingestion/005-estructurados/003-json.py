import json

# Crear una lista de clientes ficticios
clientes = [
    {
        'id': 1,
        'nombre': 'John Doe',
        'edad': 30,
        'email': 'johndoe@example.com'
    },
    {
        'id': 2,
        'nombre': 'Jane Smith',
        'edad': 35,
        'email': 'janesmith@example.com'
    },
    {
        'id': 3,
        'nombre': 'Bob Johnson',
        'edad': 28,
        'email': 'bobjohnson@example.com'
    }
]

# Especificar el nombre del archivo JSON de salida
archivo_json = 'clientes.json'

# Guardar la lista de clientes en formato JSON
with open(archivo_json, 'w') as f:
    json.dump(clientes, f, indent=4)

print(f"Se ha creado el archivo JSON '{archivo_json}' con la base de datos de clientes.")
