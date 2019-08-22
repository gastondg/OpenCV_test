import cv2
import numpy as np

# Load Yolo
weights = "/home/gastondg/Documentos/OpenCV_test/WeightConfig/yolov3-tiny.weights"
config = "/home/gastondg/Documentos/OpenCV_test/WeightConfig/yolov3-tiny.cfg"
coco = "/home/gastondg/Documentos/OpenCV_test/WeightConfig/coco.names"
net = cv2.dnn.readNet(weights, config)
classes = []
with open(coco, "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

font = cv2.FONT_HERSHEY_PLAIN
cam = cv2.VideoCapture(0)

while True:
    
    _, frame = cam.read()  

    height, width, channels = frame.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Remove noise
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
    
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)
    
    # Mostrar imagen
    cv2.imshow("Image", frame)
    # Cerrar
    k = cv2.waitKey(1)
    if k == ord('q'):
        print("Bye")
        break

cam.release()
cv2.destroyAllWindows()
