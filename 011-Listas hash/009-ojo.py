from PIL import Image
import hashlib

image_path = 'ojo.png'  # Replace 'image.jpg' with your image file path
image = Image.open(image_path)

pixel_data = image.load()

listadepixeles = []
for x in range (0,8):
    for y in range (0,8):
        listadepixeles.append(pixel_data[x,y])
cadena = ""
for pixel in listadepixeles:
    cadena += str(pixel[0])+","+str(pixel[1])+","+str(pixel[2])+";"

nombre = cadena
nombre_bytes = nombre.encode('utf-8')
resultado = hashlib.md5(nombre_bytes)
print(resultado.hexdigest())

file = open("hashes.txt","r")
lineas = file.readlines()
for linea in lineas:
    if resultado.hexdigest() == linea.split(",")[0]:
        print("coincidencia")
        print("La X es: "+linea.split(",")[1])
        print("La Y es: "+linea.split(",")[2])


