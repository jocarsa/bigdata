from PIL import Image
import hashlib
def porcion(mix,miy,anchura,altura):
    image_path = 'josevicente.png'  # Replace 'image.jpg' with your image file path
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
    #file1 = open("datos.txt", "a")
    file2 = open("hashes.txt", "a")
    cadena = ""
    for pixel in listadepixeles:
        cadena += str(pixel[0])+","+str(pixel[1])+","+str(pixel[2])+";"

    nombre = cadena
    nombre_bytes = nombre.encode('utf-8')
    resultado = hashlib.md5(nombre_bytes)
    #print(resultado.hexdigest())
    #file1.write(str(listadepixeles)+"\n")
    #file1.close()
    file2.write(resultado.hexdigest()+","+str(mix)+","+str(miy)+"\n")
    file2.close()
    

    #cropped_image.show()
for x in range(0,100-8,1):
    for y in range(0,100-8,1):
        porcion(x,y,8,8)

    
