import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def transfer_robert(img):
    # Chuyển đổi ảnh sang ảnh xám
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Tạo ma trận kernel cho toán tử Roberts
    roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    roberts_y = np.array([[0, -1], [1, 0]], dtype=np.float32)

    # Áp dụng convolution với kernel của toán tử Roberts
    roberts_x_edges = cv2.filter2D(gray_image, -1, roberts_x)
    roberts_y_edges = cv2.filter2D(gray_image, -1, roberts_y)

    roberts_x_edges = roberts_x_edges.astype(np.float32)
    roberts_y_edges = roberts_y_edges.astype(np.float32)

    # Kết hợp kết quả từ hai hướng (x và y) để tìm biên cuối cùng
    img_new = cv2.magnitude(roberts_x_edges, roberts_y_edges)
    return img_new