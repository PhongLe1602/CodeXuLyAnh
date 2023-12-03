import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def cdf(img):
    cdf_img = dict()
    for i in range(256):
        cdf_img[i] = len(img[img==i])

    for i in range(1,256):
        cdf_img[i] += cdf_img[i-1]
    return cdf_img


def histeq(img):
    cdf_img = cdf(img)
    for i in range(256):
        cdf_img[i] = int(255 * cdf_img[i]/(img.shape[0]*img.shape[1]))

    # map
    himgf = np.zeros(img.shape)
    himgf[:,:] = img

    for i in range(256):
        himgf[img==i] = cdf_img[i]


    return himgf