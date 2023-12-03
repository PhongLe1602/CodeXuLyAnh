import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def transfer_canny(img):
    # Chuyển ảnh sang ảnh xám
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc Gaussian để làm mờ ảnh và làm giảm nhiễu
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Sử dụng phương pháp Canny để phát hiện biên
    img_new = cv2.Canny(
        blurred_image, 50, 150
    )  # Thay đổi giá trị ngưỡng tùy theo hình ảnh
    return img_new