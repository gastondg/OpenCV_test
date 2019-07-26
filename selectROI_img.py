import numpy as np
import cv2
from matplotlib import pyplot as plt

def read_img(path):
    img = cv2.imread(path)
    return img

def mostrar_img(nombre, img):
    cv2.imshow("Image", img)
    return

def print_dimensiones(img):
    # img es un numpy array leido con cv2.imread
    # get dimensions of image
    dimensions = img.shape
    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    print('Image Dimension    : ', dimensions)
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)

def resize_img(img, ancho, alto):
    # img es un numpy array leido con cv2.imread
    width = ancho #1080
    height = alto #720
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    return resized

def select_roi(img):
    r = cv2.selectROI("Image", img, False, False)
    roi = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    return roi

def get_porcentaje_color(mask):
    # unos = color , ceros = ausencia de color
    ceros = len(mask[mask == 0])
    unos = len(mask[mask == 255])
    total = ceros + unos
    porcentaje_unos = unos / total * 100
    porcentaje_ceros = ceros / total * 100

    print("Cantidad de ceros: " + str(ceros))
    print("Cantidad de unos: " + str(unos))
    print("Porcentaje de unos: " + str(porcentaje_unos))
    print("Porcentaje de ceros: " + str(porcentaje_ceros))

    return porcentaje_unos, porcentaje_ceros

def get_hsv_mask(img):
    # por ahora no le paso el color, pero debería
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(imgHSV, (0, 100, 100), (10, 255, 255))
    mask2 = cv2.inRange(imgHSV, (165, 100, 100), (180, 255, 255))
    mask = mask1 + mask2
    return mask


img = read_img('imagenes/mouserojo.jpg')
print_dimensiones(img)
img = resize_img(img, 720, 720)
mostrar_img("Mouse",img)
roi = select_roi(img)
mask = get_hsv_mask(roi)
porcentaje_unos, porcentaje_ceros = get_porcentaje_color(mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
