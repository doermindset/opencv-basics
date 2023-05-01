import cv2 as cv
import numpy as np

def resize_image(image, scale=0.4):
    width = int(image.shape[1] * scale)
    length = int(image.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(image, dimensions)

img = cv.imread("#")
img = resize_image(img)
blank = np.zeros(img.shape[:2], dtype="uint8")
print(f"width {img.shape[1]}")
print(f"length {img.shape[0]}")

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, (255, 255, 255), thickness=-1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

cv.waitKey(0)