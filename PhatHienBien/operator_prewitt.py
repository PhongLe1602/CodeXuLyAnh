import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def transfer_prewitt(img):
    # Chuyển đổi ảnh sang ảnh xám
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng toán tử Prewitt theo hướng x và y
    prewitt_kernel_x = cv2.getDerivKernels(1, 0, 3, normalize=True)
    prewitt_kernel_y = cv2.getDerivKernels(0, 1, 3, normalize=True)
    prewitt_x = cv2.filter2D(
        gray_image, cv2.CV_64F, prewitt_kernel_x[0] * prewitt_kernel_x[1]
    )
    prewitt_y = cv2.filter2D(
        gray_image, cv2.CV_64F, prewitt_kernel_y[0] * prewitt_kernel_y[1]
    )

    # Kết hợp kết quả từ hai hướng (x và y) để tìm biên cuối cùng
    img_new = cv2.magnitude(prewitt_x, prewitt_y)
    return img_new