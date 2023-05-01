import cv2 as cv
import numpy as np

def resize_img(img, scale=0.40):
    width = int(img.shape[1] * scale)
    length = int(img.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("#")
img = resize_img(img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.imshow("rgb", img)

#blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

#edge cascade
canny = cv.Canny(img, 100, 175)
canny_blur = cv.Canny(blur, 100, 175)
cv.imshow("canny", canny)
cv.imshow("canny blur", canny_blur)

#dilate
dilated = cv.dilate(canny, (3,3), iterations=2)
cv.imshow("dilated", dilated)


#erode
eroded = cv.erode(dilated, (3,3), iterations=2)
cv.imshow("eroded", eroded)

#resize
resized = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv.imshow("resized", resized)


#crop
cropped = img[50:100, 200:300]
cv.imshow("cropped", cropped)
cv.waitKey(0)

