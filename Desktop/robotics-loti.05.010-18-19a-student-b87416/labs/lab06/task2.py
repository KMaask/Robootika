import cv2
import numpy as np
from time import time

trackbar_value = 90
# Open the camera
cap = cv2.VideoCapture(0)
tulem = ''
kernel = np.ones((5,5),np.uint8)

while True:    
    start = time()
    ret, frame = cap.read()
    ret, thresh = cv2.threshold(frame, trackbar_value, 255, cv2.THRESH_BINARY)
    thresholded = cv2.inRange(frame, trackbar_value)
    outimage = cv2.bitwise_and(frame, frame, mask = thresholded)
    
    erosion = cv2.erode(frame,kernel,iterations = 1)
    cv2.putText(erosion, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Blurred', erosion)
    
    '''cv2.putText(dilation, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Blurred', dilation)'''
    
    cv2.putText(frame, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0),2)
    cv2.imshow('Original', frame)
    
    lopp = time()
    tulem = str(round(1/(lopp - start), 2))
    
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()





