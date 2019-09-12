import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cam = cv2.VideoCapture(0)

while True:
    
    _, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,128),2)

    # Mostrar imagen
    cv2.imshow("Image", frame)
    # Cerrar
    k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        break
cv2.destroyAllWindows()

