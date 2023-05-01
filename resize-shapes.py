import cv2 as cv
import numpy as np


def resize_img(image, scale=0.40):

    length = int(image.shape[0] * scale)
    width = int(image.shape[1] * scale)

    dimensions = (width, length)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

    
img = cv.imread("#")

cv.imshow("img", resize_img(img))

blank = np.zeros((500, 500, 3), dtype='uint8')

blank[:] = 255,255,0

cv.imshow("blank", blank)

#rectangle
rectangle = cv.rectangle(blank, (0,0), (200,200),(255,0,0), thickness=-1)
cv.imshow("rectangle", rectangle)

#circle
circle = cv.circle(blank, (200, 200), 100, (100,100,100), thickness=-1)
cv.imshow("circle", circle)

#line
line = cv.line(blank, (100, 200), (300, 100), (200, 0, 1), thickness=2)
cv.imshow("line", line)

#text
text = cv.putText(blank, "Helllo", (100, 400), cv.FONT_HERSHEY_COMPLEX, 1.0, (100, 100, 0), thickness=3)
cv.imshow("text", text)
cv.waitKey(0)
