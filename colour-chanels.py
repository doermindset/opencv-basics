import cv2 as cv
import numpy as np

def resize_image(img, scale=0.4):
    width = int(img.shape[1] * scale)
    length = int(img.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(img, dimensions)


img = cv.imread("#")
img = resize_image(img)

blue, green, red = cv.split(img)

blank = np.zeros(img.shape[:2], dtype="uint8")


cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

canny_blue = cv.Canny(blue, 140, 255)
canny_green = cv.Canny(green, 140, 255)
canny_red = cv.Canny(red, 140, 255)

cv.imshow("Edge blue photo", canny_blue)
cv.imshow("Edge green photo", canny_green)
cv.imshow("Edge red photo", canny_red)

blank_blue = cv.merge([blue, blank, blank])
blank_green = cv.merge([blank, green, blank])
blank_red = cv.merge([blank, blank, red])
cv.imshow("Blue photo", blank_blue)
cv.imshow("Green photo", blank_green)
cv.imshow("Red photo", blank_red)
cv.waitKey(0)