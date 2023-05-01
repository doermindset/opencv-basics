import cv2 as cv

vid = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
  
while(True):
    ret, frame = vid.read()

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face_rectangle = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3)

    for (x, y, z, t) in face_rectangle:
        cv.rectangle(frame, (x,y), (x+z, y+t), (0, 0, 255), 2)
    
    cv.imshow('frame', frame)
      
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()