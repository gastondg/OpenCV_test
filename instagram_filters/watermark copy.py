import numpy as np
import cv2
from utils import image_resize

face_cascade = cv2.CascadeClassifier(
    "/home/gastondg/Documentos/OpenCV_test/instagram_filters/haarcascade_frontalface_default.xml")
#eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

img_path = '/home/gastondg/Documentos/OpenCV_test/instagram_filters/imagenes/malafama.png'
png = cv2.imread(img_path, -1)
#watermark = image_resize(logo, height=50)
#watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)
malafama_png = cv2.cvtColor(png, cv2.COLOR_BGR2BGRA)

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_h, frame_w, frame_c = frame.shape

    # overlay with 4 channels BGR and Alpha
    overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    
    # get face shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        watermark = cv2.resize(malafama_png, (w, h))
        watermark_h, watermark_w, watermark_c = watermark.shape

        # replace overlay pixels with watermark pixel values
        for i in range(0, watermark_h):
            for j in range(0, watermark_w):
                if watermark[i,j][3] != 0:
                    
                    overlay[y + i, x + j] = watermark[i,j]

    cv2.addWeighted(overlay, 1.0, frame, 1.0, 1.0, frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
