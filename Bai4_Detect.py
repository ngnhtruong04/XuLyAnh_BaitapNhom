import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai4_test.png', cv2.IMREAD_GRAYSCALE)

# Apply a binary threshold to the image
# Adjust the threshold value (127) as needed based on your specific image
_, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Optionally, you can use adaptive thresholding for more complex lighting conditions
# thresholded_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Invert the image if the background is white and the object is dark
# thresholded_image = cv2.bitwise_not(thresholded_image)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the thresholded image
cv2.imwrite('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai4_test_result.png', thresholded_image)
