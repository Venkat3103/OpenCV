import cv2
import numpy as np
from numpy.core.defchararray import center

net = cv2.dnn.readNet("yolov3.weights","yolov3.cfg")
classes = []
#read all classes present in the file coco.name

with open("coco.names","r") as f:
  classes = [line.strip() for line in f.readlines()]


#obtaining the layer names and the output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

#loading sample image
img = cv2.imread("baseball3.jpg")
#resizing the image
img = cv2.resize(img, None, fx=1.3, fy=1.3)
#obtaining the dimensions of the image
height,width,channels = img.shape

#obtaining the blob from the image
blob = cv2.dnn.blobFromImage(img, 0.00392,(416,416),(0,0,0),True,crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

#outs is the detection done - gives an array which has the information about the object detected, their position and the confidence

class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:                                       
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence>0.5:                                      #threshold for confidence
            center_x = int(detection[0]*width)                  
            center_y = int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            #cv2.circle(img,(center_x,center_y),10,(0,255,0),2)        #creating green circle of 10 pixels on the objects identified

            x = int(center_x - w/2)                                        #finding co ordinates of the rectangle (the bound)
            y = int(center_y - h/2) 

            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

            #cv2.rectangle(img,(x,y),(x+w,x+h),(0,255,0),2)             # used to outline the bound


indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)                #non max supression
print(indexes)
font = cv2.FONT_HERSHEY_PLAIN
print(len(boxes))
objects_detected = len(boxes)

colors = np.random.uniform(0, 255, size=(len(classes), 3))

for i in range(len(boxes)):
    if i in indexes:
        x,y,h,w = boxes[i]
        label = str(classes[class_ids[i]])
        confidence_val = (str(round(confidences[i],3)))
        print("Label:",label)
        print("Confidence:",confidence_val)
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label+"-"+confidence_val, (x, y), font, 1, color, 2)

cv2.imshow("Baseball",img)
cv2.waitKey(0)
cv2.destroyAllWindows()