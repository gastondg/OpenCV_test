import cv2
import numpy as np


def get_hsv_mask(img):
    # por ahora no le paso el color, pero debería
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(imgHSV, (0, 100, 100), (10, 255, 255))
    mask2 = cv2.inRange(imgHSV, (165, 100, 100), (180, 255, 255))
    mask = mask1 + mask2
    return mask

def select_roi(img):
    r = cv2.selectROI("Image", img, False, False)
    # return x, y, w, h = roi
    return r

cam = cv2.VideoCapture(0)
i=1
band = False
while cam.isOpened():
    ret, img = cam.read() #img es el frame de ese momento
    
    k = cv2.waitKey(1)
    
    if  k == ord('r'):
        # obtengo la roi
        x, y, w, h = cv2.selectROI("Cam", img, False, False)
               
        band = True
        
    elif k == ord('q'):
        print("Bye")
        break
    
    if band:
        r = cv2.rectangle(img, (x, y), (x+w, y+h), (100, 100, 255), 5)
        corte = img[y:y+h, x:x+w]
        mask = get_hsv_mask(corte)
        #res = cv2.bitwise_and(roi, roi, mask=mask)
        mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        if i == 1:
            print(mask_rgb)
            i = 2
        rect = cv2.rectangle(img, (x,y), (x+w,y+h), (100, 50, 200), 5)
        img[y:y+h, x:x+w] = mask_rgb
        cv2.imshow("Cam", img)
        #cv2.imshow("Filtro",res)
    else:
        cv2.imshow("Cam", img)

cam.release()
cv2.destroyAllWindows()
