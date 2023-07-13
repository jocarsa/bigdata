cadena = "Jose Vicente"

numero = 1
for letra in cadena:
    print(ord(letra))
    numero *= ord(letra)

print(numero)
