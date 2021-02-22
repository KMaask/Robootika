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

kernel = np.ones((5,5),np.uint8)

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

tulem = ''
while True:
    start = time()
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    #cv2.putText(frame, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    #cv2.imshow('Original', frame)
    
    lowerLimits = np.array([lB, lG, lR])
    upperLimits = np.array([hB, hG, hR])

    # Our operations on the frame come here
    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    outimage = cv2.bitwise_and(frame, frame, mask = thresholded)
    cv2.putText(outimage, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('Processed', thresholded)
    
    erosion = cv2.erode(thresholded,kernel,iterations = 1)
    cv2.putText(erosion, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Blurred', erosion)
    
    dilation = cv2.dilate(thresholded,kernel,iterations = 1)
    cv2.imshow('Dilation', dilation)
    closing = cv2.erode(dilation,kernel,iterations = 1)
    cv2.imshow('closing', closing)
 

    lopp = time()
    tulem = str(round(1/(lopp - start), 2))
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()


