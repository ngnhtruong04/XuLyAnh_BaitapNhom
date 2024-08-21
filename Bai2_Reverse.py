

import numpy as np

# Load the image manually
image = np.loadtxt('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai2.txt', dtype=np.uint8)

# Invert the image manually
inverted_image = 255 - image

# Display the original and inverted image (using matplotlib or any other method)
# Save the inverted image
np.savetxt('C:/Users/Admin/Desktop/WorkSpace/XuLyAnh/Project_Nhom/Bai2_Result.txt', inverted_image, fmt='%d')
