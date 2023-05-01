import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def resize_image(image, scale=0.4):
    width = int(image.shape[1] * scale)
    length = int(image.shape[0] * scale)
    dimensions = (width, length)

    return cv.resize(image, dimensions)

img = cv.imread("#")
img = resize_image(img)

#gray histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = cv.calcHist([gray], [0], None, [255], [0, 255])
plt.figure()
plt.title("Gray histogram")
plt.xlabel("Intensity")
plt.ylabel("No. of pixels")
plt.plot(hist)
plt.xlim([0,255])
plt.show()


blank = np.zeros(gray.shape[:2], dtype="uint8")
mask = cv.rectangle(blank, (blank.shape[1] // 2 - 100, blank.shape[0] // 2 - 100), (blank.shape[1] // 2 + 100, blank.shape[0] // 2 + 100), 255, thickness=-1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow("masked", masked)

hist_masked = cv.calcHist([gray], [0], mask, [255], [0, 255])
plt.figure()
plt.title("hist masked")
plt.xlabel("range")
plt.ylabel("no. of pixels")
plt.plot(hist_masked)
plt.xlim([0,255])
plt.show()


# colour histogram

colors = ('b', 'g', 'r')
plt.figure()
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)