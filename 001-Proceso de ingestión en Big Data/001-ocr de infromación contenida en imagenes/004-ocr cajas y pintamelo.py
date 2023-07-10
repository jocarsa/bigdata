import pytesseract
from PIL import Image, ImageDraw

imagen = Image.open('factura.png')
altura = imagen.height
cajas = pytesseract.image_to_boxes(imagen)

print(cajas)


for box in cajas.splitlines():

    character, x_start, y_start, x_end, y_end, _ = box.split(' ')

    x_start, y_start, x_end, y_end = map(int, (x_start, y_start, x_end, y_end))

    draw = ImageDraw.Draw(imagen)
    draw.rectangle([(x_start, altura-y_end), (x_end, altura-y_start)], outline='red')

    print(f"Character: {character}, Position: ({x_start}, {y_start}), ({x_end}, {y_end})")

imagen.show()
