import pytesseract
from PIL import Image

imagen = Image.open('factura.png')

cajas = pytesseract.image_to_boxes(imagen)

print(cajas)
