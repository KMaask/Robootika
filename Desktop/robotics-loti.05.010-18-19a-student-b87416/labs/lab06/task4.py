import gopigo as go
from gopigo import*
import numpy as np
import cv2
import time

kernel = np.ones((5,5),np.uint8)
#go.set_speed(55)
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
blobparams.minArea = 20
blobparams.maxArea = 500000
blobparams.minDistBetweenBlobs = 10
blobparams.filterByCircularity  = False
blobparams.filterByInertia = False
blobparams.filterByConvexity = False
detector = cv2.SimpleBlobDetector_create(blobparams)
postid = 0

while True:

    ret, frame = cap.read()
    #frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    r = [len(frame)-200, len(frame)-130, 0, len(frame[0])]
    frame=frame[r[0]:r[1], r[2]:r[3]]
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    
    lowerLimits = np.array([lH, lS, lV])
    upperLimits = np.array([hH, hS, hV])

    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    dilation = cv2.dilate(thresholded,kernel,iterations = 1)
    closing = cv2.erode(dilation,kernel,iterations = 1)
    cv2.imshow('closing', closing)
    
    keypoints = detector.detect(closing)
    for i in keypoints:
        x = i.pt[0]
        y = i.pt[1]
        print(x, y)
        cv2.putText(frame, ('x:'+str(int(x))+'y:'+ str(int(y))), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    img = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('img', img)

    #kaadrikeskpunkt
    #kahe posti keskpunkti koordinaadid
    #kaadrik == postidekeskp
    #1 posti nähes pöörab vastavalt posti asukohale nii kaua kui teine on leitud
    if len(keypoints) < 2 and postid == 0: #kui pole ühtegi posti näha
        go.right_rot()
        time.sleep(0.01)
        go.stop()
        
    if len(keypoints)==0 and postid == 1:
        go.fwd()
        

        
    if len(keypoints) == 2:
        postid = 1
        x1 = keypoints[0].pt[0]
        x2 = keypoints[1].pt[0]
        kesk = int((x1 + x2)/2)
        kaadrik = len(frame[0])/2
        if x1 > 70 and x2 < 50 or x2 > 70 and x1 < 50:
            go.fwd()
            time.sleep(4)
            go.stop()
            
        
        if x1 > 500 and x2 < 100 or x2 > 500 and x1 <100:
            go.fwd()
            time.sleep(2)
            go.stop()
            break
            
        if kaadrik >= kesk + 10:
            go.left_rot()
            time.sleep(0.01)
            go.fwd()
            go.stop()
            
        elif kaadrik < (kesk - 10):
            go.right_rot()
            time.sleep(0.01)
            go.fwd()
            go.stop()
        
        else:
            go.fwd()
            time.sleep(1)
            go.stop()
    
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        go.stop()
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()



