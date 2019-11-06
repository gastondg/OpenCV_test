from datetime import datetime
import time
import boto3

client = boto3.client("sns", "us-east-1")

a = datetime.now()

time.sleep(5)

""" k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        break """
b = datetime.now()
c = b-a
if int(c.seconds) == 5:
    texto = "prueba de sms desde archivo .py"
    print("enviando sms: "+ texto)
    try:
        client.publish(PhoneNumber="+54379154409048",
                       Message=texto)
    except Exception as e:
        print("Ocurrió un error: ")
        print(e)
print(c.seconds)
