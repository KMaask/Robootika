import numpy as np
import cv2
from time import time

# open the camera
cap = cv2.VideoCapture(0)
lB = 0
lG = 0
lR = 131
hB = 41
hG = 255
hR = 255

cv2.namedWindow("Threshold")

def updateValue(new_value):
    global lB
    lB = new_value
    return

def updateValue2(new_value):
    global lG
    lG= new_value
    return

def updateValue3(new_value):
    global lR
    lR = new_value
    return

def updateValue4(new_value):
    global hB
    hB= new_value
    return

def updateValue5(new_value):
    global hG
    hG = new_value
    return

def updateValue6(new_value):
    global hR
    hR = new_value
    return

cv2.createTrackbar("low blue", 'Threshold', lB, 255, updateValue)
cv2.createTrackbar("low green", 'Threshold', lG, 255, updateValue2)
cv2.createTrackbar("low red", 'Threshold', lR, 255, updateValue3)
cv2.createTrackbar("high blue", 'Threshold', hB, 255, updateValue4)
cv2.createTrackbar("high green", 'Threshold', hG, 255, updateValue5)
cv2.createTrackbar("high red", 'Threshold', hR, 255, updateValue6)

blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByColor = True
blobparams.blobColor = 255
#blobparams.minDistBetweenBlobs = 200
blobparams.filterByArea = True
blobparams.minArea = 50
blobparams.maxArea = 500000

detector = cv2.SimpleBlobDetector_create(blobparams)
tulem = ''
while True:
    start = time()
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.putText(frame, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    #cv2.imshow('Original', frame)
    lopp = time()
    tulem = str(round(1/(lopp - start), 2))


    #You will need this later
    #frame = cv2.cvtColor(frame, ENTER_CORRECT_CONSTANT_HERE)
    
    lowerLimits = np.array([lB, lG, lR])
    upperLimits = np.array([hB, hG, hR])

    # Our operations on the frame come here
    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    outimage = cv2.bitwise_and(frame, frame, mask = thresholded)

    cv2.imshow('Thres', thresholded)

    # Display the resulting frame
    cv2.imshow('Processed', outimage)
    
    
    keypoints = detector.detect(thresholded)
    for i in keypoints:
        x = i.pt[0]
        y = i.pt[1]
        print(x, y)
        cv2.putText(frame, ('x:'+str(int(x))+'y:'+ str(int(y))), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    img = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#Display the images
    cv2.imshow('img', img)

    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()

