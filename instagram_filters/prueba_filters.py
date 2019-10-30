import cv2
import numpy as np
from filters import Cartoonizer, CoolingFilter, WarmingFilter

cam = cv2.VideoCapture(0)
i = 1
while True:

    _, frame = cam.read()

    if frame is None:
        continue
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    pencil = WarmingFilter()
    cartoon = pencil.render(frame)
        
    # Mostrar imagen
    cv2.imshow("Image", frame)
    cv2.imshow("Sketch", sketch)

    # Cerrar
    k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        break
    i += 1

cam.release()
cv2.destroyAllWindows()
