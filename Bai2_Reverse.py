import cv2

# Load the image
image = cv2.imread('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai2.png', cv2.IMREAD_GRAYSCALE)

# Invert the image
inverted_image = cv2.bitwise_not(image)

# Display the original and inverted image
cv2.imshow('Original Image', image)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the inverted image
cv2.imwrite('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai2_Result.png', inverted_image)
