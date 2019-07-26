import cv2
import numpy as np
from datetime import datetime

def view_cam():
    
    cam = cv2.VideoCapture(0)

    lower_bound = np.array([160, 82, 82])
    upper_bound = np.array([180, 255, 255])
    i = 0
    while cam.isOpened(): # devuelve boolean
        ret, img = cam.read()
        img = cv2.flip(img, 1)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        mask1 = cv2.inRange(imgHSV, (0, 100, 100), (10, 255, 255))
        mask2 = cv2.inRange(imgHSV, (165, 100, 100), (180, 255, 255))
        mask = mask1 + mask2
        if i < 1:
            #print("mask: " + str(mask))
            ceros = len(mask[mask == 0])
            unos = len(mask[mask == 255])
            total = ceros + unos
            porcentaje_unos = unos / total * 100
            porcentaje_ceros = ceros / total * 100

            print("Cantidad de ceros: " + str(ceros))
            print("Cantidad de unos: " + str(unos))
            print("Porcentaje de unos: " + str(porcentaje_unos))
            print("Porcentaje de ceros: " + str(porcentaje_ceros))



            """ archivo = open("hello.txt", "w")
            for x in np.nditer(mask):
                archivo.write(str(x) + "\n")
            archivo.close """
            i += 1
        # poner texto
        #date = datetime.now().strftime("%d/%m/%Y")
        #text = "Fecha: " + date
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #img = cv2.putText(img, date, (5,20), font, 0.5, (0,0,0), 2)

        cv2.imshow('Front Cam', img)
        cv2.imshow('Mask Cam', mask)
        #cv2.imshow('Gray Cam', gray)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

view_cam()

#path = "/home/gdigiuseppe/Imágenes/Cámara web"
