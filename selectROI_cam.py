import cv2
import numpy as np

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, img = cam.read()
    cv2.imshow("Cam", img)

    if cv2.waitKey(ord('r')) & 0xFF == ord('r'):
        # obtengo la roi
        r = cv2.selectROI("Cam", img, False, False)
        print(r)
        select = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        cv2.imshow("seleccion", select)
        continue

    if cv2.waitKey(ord('q')) & 0xFF == ord('q'):
        print("Bye")
        break


cam.release()
cv2.destroyAllWindows()
