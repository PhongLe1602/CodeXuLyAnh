import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 

def transfer_log(img_bgr):
    # Apply log transformation method 
    c = 255 / np.log(1 + np.max(img_bgr)) 
    log_image = c * (np.log(img_bgr + 1)) 
    
    # Specify the data type so that 
    # float value will be converted to int 
    log_image = np.array(log_image, dtype = np.uint8) 
    
    # Display both images 
    # plt.imshow(img_bgr) 
    # plt.show() 
    # plt.imshow(log_image) 
    # plt.show() 
    return log_image