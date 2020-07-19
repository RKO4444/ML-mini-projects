import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img=bi,center=(x,y),radius=20,color=(255,0,0),thickness=5)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img=bi, center=(x, y), radius=20, color=(0, 100, 0), thickness=-1)
cv2.namedWindow(winname='mydrawing')
cv2.setMouseCallback('mydrawing',draw)
bi=np.zeros(shape=(500,500,3),dtype=np.int8)

while True:
    cv2.imshow('mydrawing',bi)
    if cv2.waitKey(5) ==ord('q'):
        break

cv2.destroyAllWindows()
