from PIL import Image

image_path = 'josevicente.jpg'  # Replace 'image.jpg' with your image file path
image = Image.open(image_path)

left = 100  # Starting x-coordinate of the ROI
top = 100  # Starting y-coordinate of the ROI
right = 300  # Ending x-coordinate of the ROI
bottom = 300  # Ending y-coordinate of the ROI

cropped_image = image.crop((left, top, right, bottom))
pixel_data = cropped_image.load()

listadepixeles = []
for x in range (0,200):
    for y in range (0,200):
        listadepixeles.append(pixel_data[x,y])
print(listadepixeles)
cropped_image.show()
