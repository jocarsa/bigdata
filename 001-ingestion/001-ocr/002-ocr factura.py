import pytesseract
from PIL import Image

imagen = Image.open('factura.png')

texto = pytesseract.image_to_string(imagen)

print(texto)
