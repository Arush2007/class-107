import cv2
import time
import math
p1 = 530 
p2= 300

video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()

returned, img= video.read()

box= cv2.selectROI('Tracking', img, False)
tracker.init(img,box)
print("box")
 
def drawBox(img,box):
    x,y,w,h =  int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(img , (x,y),((x+w), (y+h) ) , (255,0,255), 3,1 )
    cv2.putText(img, 'tracking', (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)   
    
def goal_track(img, box):
      x,y,w,h =  int(box[0]), int(box[1]), int(box[2]), int(box[3])
      c1= x+ int (w/2)
      c2 = y+ int(h/2)
      cv2.circle(img, (c1,c2), 2, (0,0,255), 5)
      cv2.circle(img, (int(p1), int (p2)), 2, (0,255,0), 3)

while True:
    check,img = video.read()
    success, box= tracker.update(img)
    
    if success:
        drawBox(img, box)
    else:
        cv2.putText(img, 'lost', (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        
    goal_track(img, box)   

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



