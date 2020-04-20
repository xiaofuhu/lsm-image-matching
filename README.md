# Least Squares Matching
*This repository is related to a MATH 214 class project at the University of Michigan: Linear Algebra and Least Squares Matching*

## Description
We have implemented LSM image matching in Python using image and matrix manipulation libraries including OpenCV and NumPy. 

![eqt img](https://github.com/xiaofuhu/lsm-image-matching/blob/master/96c325c6db11ddb40d09516d4681362.jpg)
The algorithm above is used in the program and takes for reference a lecture taught by Professor Cyrill Stachniss at the University of Bonn, Germany in the summer term 2015 <[Lecture](https://www.youtube.com/watch?v=JI4QhY8YXAI) Page 30>. For simplicity, we assume there is no noise in images.

## Run
Make sure the original image is named "OLD.png", the distorted image "NEW.png", and run with
```
python main.py
```
Close opened images as it runs. The result is saved as "DONT_TOUCH_ME.png"

## Results
As is shown in Fig. 1, the distorted image (mid-left) was 10 pixels left and 15 pixels up compared to the original image (top-left). Lost areas are filled with edge pixels. After running 10 iterations of our LSM process on the distorted image, we obtained the corrected output (bottom-left). Comparing the original-distorted overlay (top-right) and the original-corrected overlay (bottom-right), we observed that LSM is effective in aligning similar images.

![demo img](https://github.com/xiaofuhu/lsm-image-matching/blob/master/demo.png)
