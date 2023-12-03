import cv2
import numpy as np


def padding(img,a):
    padded_img = np.zeros((img.shape[0]+a*2,img.shape[1]+a*2))
    padded_img[a:-a,a:-a] = img
    return padded_img

def MedianFilter(img_bgr,b):
    d,c = img_bgr.shape
    a = b//2
    f_img = padding(img_bgr,a)
    filter_img = np.zeros(f_img.shape)
    for i in range(a,d+a+1):
        for j in range(a,c+a+1):
            filter_img[i,j] = np.median(f_img[i-a:i+a+1,j-a:j+a+1])
    return filter_img[a:-a,a:-a]

