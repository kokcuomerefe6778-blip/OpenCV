import numpy as np
import matplotlib.pyplot as plt

import cv2

blank_image = np.zeros(shape=(512, 512, 3),dtype=np.int8)
blank_image.shape
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.rectangle(blank_image,pt1=(384,0),pt2=(510,128),color=(0,255,0),thickness=5)
cv2.circle(blank_image, center=(100,100), radius=50, color=(255,0,0), thickness=5)   
cv2.line(blank_image,pt1=(0,0),pt2=(512,512),color=(255,255,0),thickness=5)
cv2.circle(blank_image, center=(400,400), radius=50, color=(255,0,0), thickness=-1)
cv2.rectangle(blank_image,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=5)
cv2.putText(blank_image, text="Efe", org=(10,500), fontFace=font, fontScale=4, color=(255,255,255), thickness=2, lineType=cv2.LINE_AA)


plt.imshow(blank_image)
plt.show()
