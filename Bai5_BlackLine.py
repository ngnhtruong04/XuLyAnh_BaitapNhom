import cv2
import numpy as np

# Tải hình ảnh
image = cv2.imread('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai5.png')

# Lấy kích thước của hình ảnh
height, width = image.shape[:2]

# Vẽ đường chéo màu đen
# Đường chéo từ điểm trên cùng bên trái (0, 100) đến (100, 0)
thickness = 15 # Độ dày của đường chéo
color = (0, 0, 0)  # Màu đen
cv2.line(image, (0, 100), (100, 0), color, thickness)


# Hiển thị hình ảnh
cv2.imshow('Image with Black Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu hình ảnh với đường màu đen
cv2.imwrite('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai5_result.png', image)

