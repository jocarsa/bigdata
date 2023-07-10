import pytesseract
from PIL import Image

imagen = Image.open('imagen.png')

texto = pytesseract.image_to_string(imagen)

print(texto)
