# Object detection and classification using OpenCV – YOLO Algorithm

Sample Image:
 
![image](https://user-images.githubusercontent.com/53090670/126554507-7932b5e0-b127-46a2-9f0a-57afbe00805f.png)

Detecting Objects in an Image

 ![image](https://user-images.githubusercontent.com/53090670/126554529-237bcb34-f1eb-44f6-9a63-5a7ece7380b8.png)

The circles identify each unique objects present in the image.

Marking a boundary around the identified objects
Before Non-Maximum Suppression – (many boxes for the same object – noisy) 

![image](https://user-images.githubusercontent.com/53090670/126554578-7943d7a5-76cf-415f-8d2d-9f4c112c49a5.png)

Post Non-Maximum Suppression with labels – Combining all the boxes per identified object into one.

 ![image](https://user-images.githubusercontent.com/53090670/126554600-3d5cd1ea-c890-4980-aac6-8f1e45d7257b.png)

Labels along with the confidence with which they were classified:
 
![image](https://user-images.githubusercontent.com/53090670/126554685-4123f0e5-d8b1-44ac-ba55-5c711c637824.png)

Final object detection and classification from the image with objects labelled along with their confidence levels.

![image](https://user-images.githubusercontent.com/53090670/126554719-f45d94b5-59f1-46d4-a100-e4094d13b195.png)
