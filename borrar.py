from datetime import datetime
import time

a = datetime.now()

time.sleep(5)

""" k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        break """
b = datetime.now()
c = b-a
if int(c.seconds) == 5:
    print("bien copete")
print(c.seconds)
