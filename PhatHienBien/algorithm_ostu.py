import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def transfer_ostu(img):
    # Chuyển ảnh sang ảnh xám
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng phương pháp Otsu để tìm ngưỡng tối ưu
    _, img_new = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return img_new
