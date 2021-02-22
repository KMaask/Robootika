import cv2
import numpy as np

trackbar_value = 90

blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByCircularity = False
#blobparams.minDistBetweenBlobs = 200
blobparams.filterByArea = True
blobparams.minArea = 50
blobparams.maxArea = 5000

detector = cv2.SimpleBlobDetector_create(blobparams)

def updateValue(new_value):
    # make sure to write the new value into the global variable
    global trackbar_value
    trackbar_value = new_value
    return

cv2.namedWindow("Threshold")
cv2.createTrackbar("Trackbar", 'Threshold', trackbar_value, 255, updateValue) #trackbari tegemine
#Working with image files stored in the same folder as .py file
#Load the image from the given location




#Thresholding the image (Refer to opencv.org for more details)
while True:
    #print(trackbar_value)
    img_grayscale = cv2.imread('sample02.tiff', 0)
    ret, thresh = cv2.threshold(img_grayscale, trackbar_value, 255, cv2.THRESH_BINARY)
    
    img = cv2.imread('sample02.tiff')
#Load the image from the given location in grayscale
    
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    img_grayscale = cv2.resize(img_grayscale, (0,0), fx=0.5, fy=0.5)
    thresh = cv2.resize(thresh, (0,0), fx=0.5, fy=0.5)
    
    keypoints = detector.detect(thresh)
    for i in keypoints:
        x = i.pt[0]
        y = i.pt[1]
        print(x, y)
        cv2.putText(img, ('x:'+str(int(x))+'y:'+ str(int(y))), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    
    img = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#Display the images
    cv2.imshow('Output', img)
#cv2.imshow('Grayscale', img_grayscale)
    cv2.imshow('Threshold', thresh)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    
cv2.destroyAllWindows()

