import cv2
import numpy as np

# Đọc hai hình ảnh (đã upload trước đó)
image1 = cv2.imread('Bai8_image1.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('Bai8_image2.png', cv2.IMREAD_GRAYSCALE)

# # Lấy kích thước của hình ảnh lớn nhất
max_height = min(image1.shape[0], image2.shape[0])
max_width =min(image1.shape[1], image2.shape[1])

# # Thay đổi kích thước cả hai hình ảnh thành cùng một kích thước (kích thước lớn nhất)
image1_resized = cv2.resize(image1, (max_width, max_height))
image2_resized = cv2.resize(image2, (max_width, max_height))

# Thực hiện phép trừ giữa hai hình ảnh
result_image = np.abs(image1_resized.astype(np.int16) - image2_resized.astype(np.int16)).astype(np.uint8)
# result_image = np.abs(image1.astype(np.int16) - image2.astype(np.int16)).astype(np.uint8)
# Hiển thị kết quả
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu hình ảnh kết quả
cv2.imwrite('/mnt/data/result_image.png', result_image)

