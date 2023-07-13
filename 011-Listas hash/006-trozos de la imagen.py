from PIL import Image
import hashlib
def porcion(mix,miy,anchura,altura):
    image_path = 'josevicente.jpg'  # Replace 'image.jpg' with your image file path
    image = Image.open(image_path)

    left = mix  # Starting x-coordinate of the ROI
    top = miy  # Starting y-coordinate of the ROI
    right = mix+anchura  # Ending x-coordinate of the ROI
    bottom = miy+altura  # Ending y-coordinate of the ROI

    cropped_image = image.crop((left, top, right, bottom))
    pixel_data = cropped_image.load()

    listadepixeles = []
    for x in range (0,anchura):
        for y in range (0,altura):
            listadepixeles.append(pixel_data[x,y])
    #print(listadepixeles)
    cadena = ""
    for pixel in listadepixeles:
        cadena += str(pixel[0])+","+str(pixel[1])+","+str(pixel[2])+";"

    nombre = cadena
    nombre_bytes = nombre.encode('utf-8')
    resultado = hashlib.md5(nombre_bytes)
    print(resultado.hexdigest())

    #cropped_image.show()
for x in range(0,800-64,8):
    for y in range(0,800-64,8):
        porcion(x,y,64,64)
