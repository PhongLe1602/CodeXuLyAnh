import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def knn_filter(image, k):
    kernel = np.ones((k, k), dtype=np.float32) / (
        k * k
    )  # Tạo ma trận kernel với trọng số đồng đều

    # Áp dụng convolution với kernel đã tạo
    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

def transfer_knn(img):
    img_new = knn_filter(img, 3)
    return img_new