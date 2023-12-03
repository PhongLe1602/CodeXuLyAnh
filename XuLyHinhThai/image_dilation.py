import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def Transfer_dilation(img):
    # Tạo kernel
    kernel = np.ones((5, 5), np.uint8)  # Kernel kích thước 5x5

    # Thực hiện erosion
    img_new = cv2.dilate(img, kernel, iterations=1)
    return img_new