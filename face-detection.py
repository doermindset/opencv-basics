import cv2 as cv

img = cv.imread("#")

def resize_image(img, scale=0.4):
    width = int(img.shape[1] * scale)
    length = int(img.shape[0] * scale)
    dimensions = (width, length)
    return cv.resize(img, dimensions)


img = resize_image(img)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("img gray", img_gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
faces_rectangle = haar_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3)

print(len(faces_rectangle))

for (x, y, w, z) in faces_rectangle:
    cv.rectangle(img, (x, y), (x+w, y+z), (0,0,255), 2)

cv.imshow("Detected faces", img)
cv.waitKey(0)