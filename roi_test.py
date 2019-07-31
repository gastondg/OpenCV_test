import cv2
import numpy as np

if __name__ == '__main__':
    # Read image
    img = cv2.imread("imagenes/mouserojo.jpg")
    
    roi = cv2.selectROI("Image", img, False, False)
    cv2.imshow("Image", img)
    ## Display the roi
    if roi is not None:
        x, y, w, h = roi
        mask = np.zeros_like(img, np.uint8)
        cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)
        masked = cv2.bitwise_and(img, mask)
        cv2.imshow("mask", mask)
        cv2.imshow("ROI", masked)

    k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        cv2.destroyAllWindows()
