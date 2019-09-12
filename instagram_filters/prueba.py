
import random
import os
import glob

path = '/home/gastondg/Documentos/OpenCV_test/instagram_filters/imagenes/'
extension = 'png'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
print(result)
print(type(result))

print("random.choice() to select random item from list - ", random.choice(result))
print("\nrandom.choice() to select random item from list - ", random.choice(result))
