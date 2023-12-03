import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import cv2

def ExpPlot(c, v):
    x = np.arange(0, 1, 0.01)
    y = (c + x) ** v
    plt.plot(x, y, 'r', linewidth=1)
    plt.title('FUNCTION PLOT')
    plt.xlim([0, 1]), plt.ylim([0, 1])
    plt.show()


def ExpTran(img, esp=0, gama=0.5):
    # ExpPlot(esp, gama)
    imarray = np.array(img)
    height, width = imarray.shape

    for i in range(height):
        for j in range(width):
            tmp = imarray[i, j] / 255
            tmp = int(pow(tmp + esp, gama) * 255)
            if tmp >= 0 and tmp <= 255:
                imarray[i, j] = tmp
            elif tmp > 255:
                imarray[i, j] = 255
            else:
                imarray[i, j] = 0
    return imarray