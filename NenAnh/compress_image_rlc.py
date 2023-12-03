import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
# Hàm nén ảnh bằng RLC
def rlc_encode(image):
    pixels = list(image.getdata())
    width, height = image.size
    encoded_data = []

    for y in range(height):
        current_run = 1
        current_pixel = pixels[y * width]

        for x in range(1, width):
            pixel = pixels[y * width + x]
            if pixel == current_pixel:
                current_run += 1
            else:
                encoded_data.append((current_pixel, current_run))
                current_pixel = pixel
                current_run = 1

        encoded_data.append((current_pixel, current_run))

    return encoded_data