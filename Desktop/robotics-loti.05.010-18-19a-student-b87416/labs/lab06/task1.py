import cv2
import numpy as np
from time import time

# Open the camera
cap = cv2.VideoCapture(0)
tulem = ''
while True:
    start = time()
    ret, frame = cap.read()
    #print(len(frame), len(frame[0])) pildi suuruse leidmine
    #frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    blur = cv2.blur(frame, (11,11))
    #blur = cv2.GaussianBlur(frame, (21,21), 0)
    
    cv2.putText(blur, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Blur', blur)
    
    lopp = time()
    tulem = str(round(1/(lopp - start), 2))
    
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()




