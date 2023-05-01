import cv2 as cv
import numpy as np

def resize_img(img, scale=0.40):
    width = int(img.shape[1] * scale)
    length = int(img.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("#")
img = resize_img(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple thrashold
threshold, thresh = cv.threshold(gray, 160, 255, type=cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

#adaptive thrasholding
adaptive_thrasholding = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("adaptive", adaptive_thrasholding)

cv.waitKey(0)