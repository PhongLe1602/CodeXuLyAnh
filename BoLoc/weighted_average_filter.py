import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def transfer_weighted_average(img):
    # Định nghĩa ma trận trọng số
    kernel = (
        np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16
    )  # Tính trung bình để chuẩn hóa
    img_new = cv2.filter2D(img, -1, kernel)
    return  img_new