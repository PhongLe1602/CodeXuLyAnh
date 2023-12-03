import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
def transfer_sobel(img):
    # Chuyển đổi ảnh sang ảnh xám
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng toán tử Sobel theo hướng x và y
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Kết hợp kết quả từ hai hướng (x và y) để tìm biên cuối cùng
    img_new = cv2.magnitude(sobel_x, sobel_y) 
    return img_new