import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai3.png')

# Get the dimensions of the image
height, width = image.shape[:2]

# Create an empty array for the rotated image
rotated_image = np.zeros((height, width, 3), dtype=np.uint8)

# Rotate the image 180 degrees
for i in range(height):
    for j in range(width):
        rotated_image[height - 1 - i, width - 1 - j] = image[i, j]

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save the rotated image
cv2.imwrite('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai3_Result.png', rotated_image)
