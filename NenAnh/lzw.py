import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

def compress_lzw(img):
    pixels = list(img.getdata())
    dictionary = {i: chr(i) for i in range(256)}
    compressed_data = []
    current_code = 256
    sequence = pixels[0]

    for pixel in pixels[1:]:
        combined_sequence = sequence + pixel
        if combined_sequence in dictionary:
            sequence = combined_sequence
        else:
            compressed_data.append(dictionary[sequence])
            dictionary[combined_sequence] = current_code
            current_code += 1
            sequence = pixel

    compressed_data.append(dictionary[sequence])
    return compressed_data, dictionary