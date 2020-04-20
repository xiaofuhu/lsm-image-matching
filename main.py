# Copyright 2020, Fuhu Xiao, All rights reserved.

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from shift_img import shift_img

IMG_A = "NEW.png"
IMG_B = "OLD.png"
WORK = "DONT_TOUCH_ME.png"
IMG_SIZE = (220, 290)
EPOCH = 10


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def init_img_size(img_name):
    global IMG_SIZE
    img = mpimg.imread(img_name)     
    gray = rgb2gray(img)
    gray = np.array(gray)
    IMG_SIZE = np.shape(gray)

def serialize_image(img_name):
    img = mpimg.imread(img_name)     
    gray = rgb2gray(img)
    gray = np.array(gray)
    gray = gray.flatten()
    return gray

def gen_grad(img):
    global IMG_SIZE
    result = np.ndarray((len(img), 2))
    img = np.reshape(img, IMG_SIZE)
    for i, ei in enumerate(img):
        for j, ej in enumerate(ei):
            if j > 0 and j < IMG_SIZE[1] - 1:
                result[i * IMG_SIZE[1] + j][0] = (img[i][j + 1] - img[i][j - 1]) / 2
            if i > 0 and i < IMG_SIZE[0] - 1:
                result[i * IMG_SIZE[1] + j][1] = (img[i + 1][j] - img[i - 1][j]) / 2
    return result

def calc_LSM_sol(mat, dl):
    mat_t = np.transpose(mat)
    prod = np.matmul(mat_t, mat)
    inverse = np.linalg.inv(prod)
    new_mat = np.matmul(inverse, mat_t)
    lsm = np.matmul(new_mat, dl)
    return lsm

def iterate(new, old):
    img_observed = serialize_image(new)
    img_original = serialize_image(old)
    delta_l = img_observed - img_original
    A_matrix = gen_grad(img_original)
    result = calc_LSM_sol(A_matrix, delta_l)
    return result

def save_to_work(result):
    mpimg.imsave(WORK, result)

def load_from_work():
    return np.array(mpimg.imread(WORK))

if __name__ == "__main__":
    init_img_size(IMG_A)
    save_to_work(mpimg.imread(IMG_A))
    for i in range(EPOCH):
        result = iterate(WORK, IMG_B)
        print((int(result[0]), int(result[1])))
        tmp = shift_img(load_from_work(), int(result[0] * 15), int(result[1] * 15))
        plt.imshow(tmp)
        plt.show()
        save_to_work(tmp)

    print("finish")