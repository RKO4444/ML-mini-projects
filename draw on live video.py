import cv2
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,580)
def draw(event,x,y,flags,param):
    global pt1,pt2,top_left_clicked,bottom_right_clicked
    if event==cv2.EVENT_LBUTTONDOWN:
        if top_left_clicked == True and bottom_right_clicked==True:
            pt1=(0,0)
            pt2=(0,0)

            top_left_clicked=False
            bottom_right_clicked=False
                       
    if top_left_clicked==False:
        pt1=(x,y)
        top_left_clicked=True

    elif bottom_right_clicked==False:
        pt2=(x,y)
        bottom_right_clicked=True

top_left_clicked=False
bottom_right_clicked=False

cv2.namedWindow('test')
cv2.setMouseCallback('test',draw)


while True:
    ret,frame=cap.read()

    if top_left_clicked == True:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)

    if top_left_clicked== True and  bottom_right_clicked== True:
        cv2.rectangle(frame,pt1,pt2,(255,0,0),3)





    cv2.imshow('frame',frame)                          


    if cv2.waitKey(5) & 0xff==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()