import numpy as np
import cv2

# Kích thước của chữ B
height = 250
width = 220
#width ban đầu là 240 để tiện cho việc chia 3 mỗi phần 80, bớt đi 20 do bên phải bị dư nhiều
# Tạo ảnh với màu đen (giá trị 0)
letter_b = np.zeros((height, width), dtype=np.uint8)

# Vẽ chữ B bằng cách tạo các hình chữ nhật màu trắng (giá trị 255)
# Vùng trên của chữ B
letter_b[0:25, 160:240] = 255  # Phần phải trên
letter_b[50:100, 80:160] = 255  # Lỗ hổng trên
letter_b[150:200, 80: 160] = 255 # Lỗ hổng dưới

letter_b[225:250, 160:240]=255 #Phần phải dưới
letter_b[115:135, 160:240] = 255 #Phần phải giữa
# Hiển thị hình ảnh chữ B
cv2.imshow('Letter B', letter_b)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Lưu hình ảnh chữ B dưới dạng PNG
cv2.imwrite('letter_b.png', letter_b)
