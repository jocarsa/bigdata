import cv2

# Load source and target images
source_image = cv2.imread('josevicente.jpg')
target_image = cv2.imread('keanu.jpg')

# Resize the source image to match the target image size
source_image = cv2.resize(source_image, (target_image.shape[1], target_image.shape[0]))

# Convert the images to grayscale
source_gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
target_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the images
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
source_faces = face_cascade.detectMultiScale(source_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
target_faces = face_cascade.detectMultiScale(target_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Iterate over detected faces
for (x, y, w, h) in source_faces:
    # Extract the region of interest (ROI) from the source image
    source_roi = source_image[y:y+h, x:x+w]

    # Find the corresponding face in the target image
    # (You can use more advanced techniques here, such as facial landmark detection)
    # For simplicity, let's assume the first detected face in the target image is the target face
    (tx, ty, tw, th) = target_faces[0]
    
    # Resize the source ROI to match the size of the target face
    source_roi = cv2.resize(source_roi, (tw, th))
    
    # Replace the target face with the source ROI
    target_image[ty:ty+th, tx:tx+tw] = source_roi

# Display the result
cv2.imshow('Deepfake Image', target_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
