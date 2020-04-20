# lsm-image-matching
Least Squares Method (LSM) for image alignment - MATH 214

We have implemented LSM image matching in Python using image and matrix manipulation libraries including OpenCV and NumPy. 

The algorithm used takes for reference a lecture taught by Professor Cyrill Stachniss at the University of Bonn, Germany in the summer term 2015 http://github.com - automatic!
[GitHub](http://github.com). However, for simplicity, we assume there is no noise in images.

As is shown in Fig. 1, the distorted image (mid-left) was 10 pixels left and 15 pixels up compared to the original image (top-left). Lost areas are filled with edge pixels. After running 10 iterations of our LSM process on the distorted image, we obtained the corrected output (bottom-left). Comparing the original-distorted overlay (top-right) and the original-corrected overlay (bottom-right), we observed that LSM is effective in aligning similar images.

![demo img](https://github.com/xiaofuhu/lsm-image-matching/blob/master/demo.png)
