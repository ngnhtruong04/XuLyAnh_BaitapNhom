import cv2
import numpy as np

# Define the size of the image
height, width = 400, 400

# Create an empty image with a single channel (grayscale)
gradient_image = np.zeros((height, width), dtype=np.uint8)

# Fill the image with a gradient
for i in range(height):
    intensity = 255 - int((i / height) * 255)  # Calculate intensity from white (255) to black (0)
    gradient_image[i, :] = intensity

# Display the gradient image
cv2.imshow('White-to-Black Gradient', gradient_image)
cv2.waitKey(0)
cv2.destroyAllWindows()