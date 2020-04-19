import numpy as np 
import matplotlib.pyplot as plt 

IMG_A = "img1.jpg"
IMG_B = "img2.jpg"

def linearize_image(img_name):
    pass

def gen_grad(img):
    pass

def calc_LSM_sol(mat, dl):
    pass

def save_result(result):
    pass

if __name__ == "__main__":
    img_observed = linearize_image(IMG_A)
    img_original = linearize_image(IMG_B)
    delta_l = img_a - img_b
    A_matrix = gen_grad(img_original)
    result = calc_LSM_sol(A_matrix, delta_l)
    save_result(result)