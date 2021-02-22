import numpy as np
import cv2
from time import time

# Open the camera
cap = cv2.VideoCapture(0)
tulem = ''
while True:
    start = time()
    ret, frame = cap.read()
    

    # Write some text onto the frame
    cv2.putText(frame, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show this image on a window named "Original"
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

