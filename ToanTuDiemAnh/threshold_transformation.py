import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 

def transfer_thresholding(img_bgr,threshold):
    # Sao chép ảnh để tránh thay đổi ảnh gốc
    result = img_bgr.copy()
    # Lặp qua từng pixel và áp dụng phân ngưỡng
    result[result <= threshold] = 0  # Gán giá trị 0 cho pixel nhỏ hơn hoặc bằng ngưỡng
    result[result > threshold] = 255  # Gán giá trị 255 cho pixel lớn hơn ngưỡng
    return  result