import numpy as np
import cv2

# Set the size of the chessboard
rows, cols = 8, 8  # 8x8 chessboard
square_size = 50   # Size of each square in pixels

# Create a black square
black_square = np.zeros((square_size, square_size), dtype=np.uint8)

# Create a white square
white_square = np.ones((square_size, square_size), dtype=np.uint8) * 255

# Initialize the chessboard with zeros (black squares)
chessboard = np.zeros((rows * square_size, cols * square_size), dtype=np.uint8)

# Fill the chessboard with black and white squares
for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 0:
            chessboard[row * square_size:(row + 1) * square_size, col * square_size:(col + 1) * square_size] = white_square
        else:
            chessboard[row * square_size:(row + 1) * square_size, col * square_size:(col + 1) * square_size] = black_square

# Display the chessboard
cv2.imshow('Chessboard', chessboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image if needed
cv2.imwrite('chessboard.png', chessboard)



import numpy as np
import cv2

# Kích thước của bàn cờ
rows, cols = 8, 8  # Bàn cờ 8x8
square_size = 50   # Kích thước của mỗi ô vuông (tính theo pixel)

# Khởi tạo bàn cờ với màu đen
chessboard = np.zeros((rows * square_size, cols * square_size), dtype=np.uint8)

# Vẽ bàn cờ bằng cách lấp đầy các ô đen và trắng
for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 0:
            chessboard[row * square_size:(row + 1) * square_size, col * square_size:(col + 1) * square_size] = 255  # Ô trắng
        # Ô đen đã mặc định là 0 nên không cần thay đổi gì

# Hiển thị bàn cờ (nếu muốn)
cv2.imshow('Chessboard', chessboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh dưới dạng tệp PNG
cv2.imwrite('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai1_result.png', chessboard)

