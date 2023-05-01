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

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("SobelX", sobelx)
cv.imshow("SobelY", sobely)
cv.imshow("SobelXY", combine_sobel)

#Canny
canny = cv.Canny(gray, 160, 255)
cv.imshow("Canny", canny)


cv.waitKey(0)