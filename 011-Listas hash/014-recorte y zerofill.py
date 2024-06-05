

def hashJoseVicente(cadena):
    numero = 1
    for letra in cadena:
        numero *= ord(letra)
    return "{:10d}".format(int(str(numero)[:10]))

print(hashJoseVicente("Jose Vicente"))
print(hashJoseVicente("Jose Vicente"))
print(hashJoseVicente("Juan"))
print(hashJoseVicente("Juan"))
print(hashJoseVicente("Esta es una prueba que voy a hacer a ver si obtengo un numero demasiado grande para Python"))
