import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import cv2

def Close_image(img):
     # Tạo kernel
    kernel = np.ones((5, 5), np.uint8)  # Kernel kích thước 5x5

    # Thực hiện dilation
    dilated_image = cv2.dilate(img, kernel, iterations=1)

    # Thực hiện erosion trên ảnh sau khi đã được dilation
    img_new = cv2.erode(dilated_image, kernel, iterations=1)
    return img_new
