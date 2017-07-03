import cv2
import numpy as np
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('H High','image',0,255,nothing)
cv2.createTrackbar('H Low','image',0,255,nothing)
cv2.createTrackbar('S High','image',0,255,nothing)
cv2.createTrackbar('S Low','image',0,255,nothing)
cv2.createTrackbar('V High','image',0,255,nothing)
cv2.createTrackbar('V Low','image',0,255,nothing)


cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv2.imshow('image',img)
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF

   
    if k == 27:
        break
    # get current positions of four trackbars
    hL = cv2.getTrackbarPos('H Low','image')
    sL = cv2.getTrackbarPos('S Low','image')
    vL = cv2.getTrackbarPos('V Low','image')
    hH = cv2.getTrackbarPos('H High','image')
    sH = cv2.getTrackbarPos('S High','image')
    vH = cv2.getTrackbarPos('V High','image')

    
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([hL,sL,vL])
    upper_hsv = np.array([hH,sH,vH])
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    img = mask
        

        
cv2.destroyAllWindows()
    

