import cv2
import matplotlib.pyplot as plt
import numpy as np
import math      
            
def Open_image(img):
                    
    # Tạo kernel
    kernel = np.ones((5, 5), np.uint8)  # Kernel kích thước 5x5

    # Thực hiện erosion
    eroded_image = cv2.erode(img, kernel, iterations=1)

    # Thực hiện dilation trên ảnh sau khi đã được erosion
    img_new = cv2.dilate(eroded_image, kernel, iterations=1)
    return img_new