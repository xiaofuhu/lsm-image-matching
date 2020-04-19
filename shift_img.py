import numpy as np 
import cv2
import matplotlib.pyplot as plt 
from PIL import Image

SHIFT_X = -10
SHIFT_Y = 15


def shift_img(img, x, y):
    for i in range(len(img)):
        if (x >= 0):
            for j in reversed(range(len(img[i]))):
                if j >= x:
                    img[i][j] = img[i][j - x]
                else:
                    img[i][j] = img[i][0]
        else:
            for j in range(len(img[i])):
                if j < len(img[i]) + x:
                    img[i][j] = img[i][j - x]
                else:
                    img[i][j] = img[i][len(img[i]) - 1]

    if (y >= 0):
        for i in reversed(range(len(img))):
            for j in range(len(img[i])):   
                if i >= y:
                    img[i][j] = img[i - y][j]
                else:
                    img[i][j] = img[0][j]
    else:
        for i in range(len(img)):
            if i < len(img) + y:
                for j in range(len(img[i])):
                    img[i][j] = img[i - y][j]
            else: 
                for j in range(len(img[i])):
                    img[i][j] = img[len(img) - 1][j]
    return img


if __name__ == "__main__":
    img = cv2.imread('OLD.png')
    cv2.imwrite("NEW.png", shift_img(img, SHIFT_X, SHIFT_Y))
    