import cv2
import numpy as np
import mediapipe as mp

# Load the source and target images
source_image = cv2.imread('josevicente.jpg')
target_image = cv2.imread('keanu.jpg')

# Initialize the face mesh model from Mediapipe
mp_face_mesh = mp.solutions.face_mesh.FaceMesh()

# Detect landmarks on the source and target images
source_results = mp_face_mesh.process(cv2.cvtColor(source_image, cv2.COLOR_BGR2RGB))
target_results = mp_face_mesh.process(cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB))

# Extract the facial landmarks from the results
source_landmarks = []
for face_landmarks in source_results.multi_face_landmarks:
    for landmark in face_landmarks.landmark:
        source_landmarks.append([landmark.x, landmark.y])

target_landmarks = []
for face_landmarks in target_results.multi_face_landmarks:
    for landmark in face_landmarks.landmark:
        target_landmarks.append([landmark.x, landmark.y])

# Convert landmarks to NumPy arrays
source_landmarks = np.array(source_landmarks)
target_landmarks = np.array(target_landmarks)

# Compute the affine transformation matrix
transformation_matrix, _ = cv2.estimateAffinePartial2D(source_landmarks, target_landmarks)

# Warp the source face to match the target face geometry
warp_image = cv2.warpAffine(source_image, transformation_matrix, (target_image.shape[1], target_image.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

# Create a mask of the target face region
mask = np.zeros_like(target_image)
cv2.fillConvexPoly(mask, np.int32(target_landmarks), (255, 255, 255))

# Extract the face region from the target image
masked_target_image = cv2.bitwise_and(target_image, mask)

# Blend the warped source face onto the target image
final_image = cv2.add(masked_target_image, warp_image)

# Display the final result
cv2.imshow('Face Swapped Image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
