import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

IMG_A = "M.png"
IMG_B = "M.png"

IMG_SIZE = (220, 290)

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def linearize_image(img_name):
    img = mpimg.imread(img_name)     
    gray = rgb2gray(img)
    gray = np.array(gray)
    IMG_SIZE = np.shape(gray)
    gray = gray.flatten()
    return gray

def gen_grad(img):
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

def save_result(result):
    pass

if __name__ == "__main__":
    img_observed = linearize_image(IMG_A)
    img_original = linearize_image(IMG_B)
    delta_l = img_observed - img_original
    A_matrix = gen_grad(img_original)
    result = calc_LSM_sol(A_matrix, delta_l)
    print(result)
    save_result(result)