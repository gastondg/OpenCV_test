import cv2
import numpy as np
from datetime import datetime

def view_cam():
    
    cam = cv2.VideoCapture(0)

    lower_bound = np.array([150, 49, 217])
    upper_bound = np.array([177, 170, 165])

    while cam.isOpened(): # devuelve boolean
        ret, img = cam.read()
        img = cv2.flip(img, 1)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #mask = cv2.inRange(imgHSV, lower_bound, upper_bound)
        #mask1 = cv2.inRange(imgHSV, (166,146,60), (186, 171, 178))
        #mask2 = cv2.inRange(imgHSV, (151, 40, 180), (173, 82, 275))
        mask1 = cv2.inRange(imgHSV, (0, 100, 100), (10, 255, 255))
        mask2 = cv2.inRange(imgHSV, (160, 100, 100), (179, 255, 255))
        
        mask = mask1 + mask2
        print(mask.size)
        date = datetime.now().strftime("%d/%m/%Y")
        #text = "Fecha: " + date
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.putText(img, date, (5,20), font, 0.5, (0,0,0), 2)

        cv2.imshow('Front Cam', img)
        cv2.imshow('Mask Cam', mask)
        #cv2.imshow('Gray Cam', gray)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

view_cam()

#path = "/home/gdigiuseppe/Imágenes/Cámara web"
