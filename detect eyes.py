"""import cv2
import numpy as np
import matplotlib.pyplot as plt

classi=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('IMG_20200413_031050.jpg')
fix_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

faces=classi.detectMultiScale(fix_img,1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(fix_img,(x,y),(x+w,y+h),(255,0,0),6)
plt.imshow(fix_img)
plt.show()"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('50-Long-Haircuts-Hairstyle-Tips-for-Men-2.jpg')
fix_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


eye_class=cv2.CascadeClassifier('harrCascades\haarcascade_eye.xml')
classi=cv2.CascadeClassifier('harrCascades\haarcascade_frontalface_default.xml')


faces=classi.detectMultiScale(fix_img)
eye=eye_class.detectMultiScale(fix_img)


for (ix,iy,iw,ih) in eye:
    cv2.rectangle(fix_img,(ix,iy),(ix+iw,iy+ih),(0,255,0),4)


for (x, y, w, h) in faces:
    cv2.rectangle(fix_img, (x, y), (x + w, y + h), (255, 0, 0), 6)

plt.imshow(fix_img)
plt.show()