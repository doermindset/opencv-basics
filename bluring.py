import cv2 as cv
import numpy as np

def resize_image(img, scale=0.4):
    width = int(img.shape[1] * scale)
    length = int(img.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(img, dimensions)


img = cv.imread("#")
img = resize_image(img)

#gaussian blur
gaussian_blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("gausian blur", gaussian_blur)

#average blur
average_blur = cv.blur(img, (3,3))
cv.imshow("average blur", average_blur)

#median blur
median_blur = cv.medianBlur(img, 3)
cv.imshow("median blur", median_blur)

#bilateral blur
bilateral_blur = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow("bilateral blur", bilateral_blur)
cv.waitKey(0)