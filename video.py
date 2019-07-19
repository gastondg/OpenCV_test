
import cv2
import numpy as np

def view_cam():
    
    cam = cv2.VideoCapture(0)

    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 255)

    ret, im = cam.read()
    locy = int(im.shape[0]/2) # the text location will be in the middle
    locx = int(im.shape[1]/2) #           of the frame for this example

    while True:
        ret, im = cam.read()
        cv2.putText(im, "Success!", (locx, locy), fontFace, fontScale, fontColor) 
        cv2.imshow('Front Cam', im)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

view_cam()
