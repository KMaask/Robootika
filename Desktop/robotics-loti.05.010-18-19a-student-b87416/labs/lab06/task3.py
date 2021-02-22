import gopigo as go
import numpy as np
import cv2
from time import time

kernel = np.ones((5,5),np.uint8)
go.set_speed(25)
cap = cv2.VideoCapture(0)
lH = 0
lS = 90
lV = 81
hH = 11
hS = 255
hV = 255

cv2.namedWindow("Threshold")

def updateValue(new_value):
    global lH
    lH = new_value
    return

def updateValue2(new_value):
    global lS
    lS= new_value
    return

def updateValue3(new_value):
    global lV
    lV = new_value
    return

def updateValue4(new_value):
    global hH
    hH= new_value
    return

def updateValue5(new_value):
    global hS
    hS = new_value
    return

def updateValue6(new_value):
    global hV
    hV = new_value
    return

cv2.createTrackbar("low hue", 'Threshold', lH, 255, updateValue)
cv2.createTrackbar("low saturation", 'Threshold', lS, 255, updateValue2)
cv2.createTrackbar("low value", 'Threshold', lV, 255, updateValue3)
cv2.createTrackbar("high hue", 'Threshold', hH, 255, updateValue4)
cv2.createTrackbar("high saturation", 'Threshold', hS, 255, updateValue5)
cv2.createTrackbar("high value", 'Threshold', hV, 255, updateValue6)

blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByColor = True
blobparams.blobColor = 255
blobparams.filterByArea = True
blobparams.minArea = 50
blobparams.maxArea = 500000

detector = cv2.SimpleBlobDetector_create(blobparams)
tulem = ''
while True:
    start = time()
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.putText(frame, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    lowerLimits = np.array([lH, lS, lV])
    upperLimits = np.array([hH, hS, hV])

    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    dilation = cv2.dilate(thresholded,kernel,iterations = 1)
    closing = cv2.erode(dilation,kernel,iterations = 1)
    cv2.imshow('closing', closing)
 
    #outimage = cv2.bitwise_and(frame, frame, mask = thresholded)
    #cv2.imshow('Thres', thresholded)
    #cv2.imshow('Processed', outimage)
    
    keypoints = detector.detect(closing)
    for i in keypoints:
        x = i.pt[0]
        y = i.pt[1]
        print(x, y)
        cv2.putText(frame, ('x:'+str(int(x))+'y:'+ str(int(y))), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    img = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('img', img)
    
    if len(keypoints)> 0:
        x = keypoints[0].pt[0]
        kaadrik = len(frame[0])/2
        if x >= kaadrik + 20:
            go.right_rot()
        elif x <= kaadrik - 20:
            go.left_rot()
        else:
            go.stop()
    lopp = time()
    tulem = str(round(1/(lopp - start), 2))
    
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        go.stop()
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()


