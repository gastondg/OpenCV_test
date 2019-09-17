import cv2
import numpy as np
from datetime import datetime

from utils import CFEVideoConf

cap = cv2.VideoCapture(0)

save_path = 'prueba720p.mp4'
frames_per_seconds = 24
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type,
                      frames_per_seconds, config.dims)
start_time = datetime.now()
while True:

    _, frame = cap.read()
    
    if frame is None:
        continue

    # grabar 30 segundos y después cortar
    out.write(frame)
    b = datetime.now()
    fin_time = b-start_time
    if int(fin_time.seconds) == 10:
        # finalizar el video
        break

out.release()
cap.release()



