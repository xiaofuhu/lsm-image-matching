import numpy as np 
import cv2
import matplotlib.pyplot as plt 
from PIL import Image

SHIFT = 50

if __name__ == "__main__":
    img1 = cv2.imread('M.png')  
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    for i in img1:
        for j, e in enumerate(reversed(i)):
            if j > SHIFT:
                e = img1[j + SHIFT];
    cv2.imwrite("NEW.png", img1)
    