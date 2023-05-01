import cv2 as cv
import numpy as np

def resize_image(image, scale=0.4):
    width = int(image.shape[1] * scale)
    length = int(image.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(image, dimensions)

img = cv.imread("#")
img = resize_image(img)

cv.imshow("image", img)

#Method1
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(gray, 130, 255)
cv.imshow("canny", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

blank1 = np.zeros(img.shape[:2], dtype="uint8")
cv.drawContours(blank1, contours, -1, 255, thickness=2)
cv.imshow("contour 1", blank1)


#Method2

img_cont, threshold = cv.threshold(gray, 130, 255, cv.THRESH_BINARY)
cv.imshow("threshold", threshold)

contours2, hierarchies2 = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours2))

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank", blank)

cv.drawContours(blank, contours2, -1, 255)
cv.imshow("contours", blank)



cv.waitKey(0)