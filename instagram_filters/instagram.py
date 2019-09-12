import numpy as np
import cv2
import os
import glob
import random

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

path = '/home/gastondg/Documentos/OpenCV_test/instagram_filters/imagenes/'
extension = 'png'
os.chdir(path)
imagenes = glob.glob('*.{}'.format(extension))

FILTRO = cv2.imread(random.choice(imagenes),-1)
FILTRO = cv2.cvtColor(FILTRO, cv2.COLOR_BGR2BGRA)

def get_random_filter(i, imagenes):
    global FILTRO
    if ((i % 100) == 0):
        # seleccionar imagen random para el filtro
        FILTRO = cv2.imread(random.choice(imagenes), -1)
        FILTRO = cv2.cvtColor(FILTRO, cv2.COLOR_BGR2BGRA)
        return FILTRO
    else:
        return FILTRO


cam = cv2.VideoCapture(0)
i = 1
while True:

    _, frame = cam.read()

    if frame is None:
        continue
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        
        filtro = get_random_filter(i, imagenes)
        resized_image = cv2.resize(filtro, (w, h))
        # , interpolation=cv2.INTER_AREA

        frame[y:y+h, x:x+w] = resized_image

        #frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 128), 2)

    # Mostrar imagen
    cv2.imshow("Image", frame)
    # Cerrar
    k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        break
    i += 1

cv2.destroyAllWindows()
