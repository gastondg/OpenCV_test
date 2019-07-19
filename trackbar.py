import cv2
import numpy as np

def nothing(x):
    pass

cam = cv2.VideoCapture(0)

cv2.namedWindow("hsv_picker")
# defino lower
cv2.createTrackbar("Low H", "hsv_picker", 0, 255, nothing)
cv2.createTrackbar("Low S", "hsv_picker", 0, 255, nothing)
cv2.createTrackbar("Low V", "hsv_picker", 0, 255, nothing)
# defino upper
cv2.createTrackbar("Up H", "hsv_picker", 255, 255, nothing)
cv2.createTrackbar("Up S", "hsv_picker", 255, 255, nothing)
cv2.createTrackbar("Up V", "hsv_picker", 255, 255, nothing)



while cam.isOpened():
    ret, img = cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_h = cv2.getTrackbarPos("Low H", "hsv_picker")
    low_s = cv2.getTrackbarPos("Low S", "hsv_picker")
    low_v = cv2.getTrackbarPos("Low V", "hsv_picker")

    up_h = cv2.getTrackbarPos("Up H", "hsv_picker")
    up_s = cv2.getTrackbarPos("Up S", "hsv_picker")
    up_v = cv2.getTrackbarPos("Up V", "hsv_picker")

    lower_color = np.array([low_h, low_s, low_v])
    upper_color = np.array([up_h, up_s, up_v])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Cam", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
