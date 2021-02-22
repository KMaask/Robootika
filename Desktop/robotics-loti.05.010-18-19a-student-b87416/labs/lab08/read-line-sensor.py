#!/usr/bin/env python3
# coding=utf-8
import serial
import gopigo as go
import time
import cv2
import json
import os
import time
import numpy as np
import _thread

img_orig = cv2.imread('map.png')
go.set_speed(40)
us_pos = 0
enc_pos = 0
cam_pos = 0
scale = 0.5
vasak = go.enc_read(0)
parem = go.enc_read(1)

running = True

def getDistanceWithCam(blobSize):
    if blobSize > 0:
        return 59915.85/blobSize - 117.47
    return -1

'''
A function to run in a separate thread from the line sensor. Since we want to
read the line sensors as quickly as possible then we would want to run slower
operations such as image processing here. This function will run in a separate thread
as long as the 'running' variable is True. This variable is only set to false
when the main thread is stopped.
'''
def slowThread():
    global us_pos
    global enc_pos
    global cam_pos
    global scale
    global running
    lH = 0
    lS = 71
    lV = 112
    hH = 255
    hS = 255
    hV = 255
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Trackbar')
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

    cv2.createTrackbar("low hue", 'Trackbar', lH, 255, updateValue)
    cv2.createTrackbar("low saturation", 'Trackbar', lS, 255, updateValue2)
    cv2.createTrackbar("low value", 'Trackbar', lV, 255, updateValue3)
    cv2.createTrackbar("high hue", 'Trackbar', hH, 255, updateValue4)
    cv2.createTrackbar("high saturation", 'Trackbar', hS, 255, updateValue5)
    cv2.createTrackbar("high value", 'Trackbar', hV, 255, updateValue6)
    blobparams = cv2.SimpleBlobDetector_Params()
    blobparams.filterByCircularity = False
    #blobparams.filterByColor = False
        #blobparams.blobColor = 255
    blobparams.minDistBetweenBlobs = 150
    blobparams.filterByArea = True
    blobparams.minArea = 200 
    blobparams.maxArea = 80000000

    detector = cv2.SimpleBlobDetector_create(blobparams)

    while running:
        # Slower code goes here
        ENC1_MOVED_TICKS = go.enc_read(0)-vasak 
        ENC2_MOVED_TICKS = go.enc_read(1)-parem 
        MOVED_TICKS = int((ENC1_MOVED_TICKS + ENC2_MOVED_TICKS)/2)
        enc_pos = 1478 - MOVED_TICKS*11.34
        #print('enc_pos: ', enc_pos)
        

        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame = cv2.resize(frame, (0,0), fx=0.2, fy=0.2)
        lowerLimits = np.array([lH, lS, lV])
        upperLimits = np.array([hH, hS, hV])
        
        # Our operations on the frame come here
        thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
        outimage = cv2.bitwise_and(frame, frame, mask = thresholded)
        outimage = cv2.bitwise_not(thresholded)
        
        keypoints = detector.detect(outimage)
        outimage = cv2.drawKeypoints(outimage, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        if len(keypoints)>0:
            blobSize = int(keypoints[0].size)
            cam_pos = getDistanceWithCam(blobSize)
            print('cam_pos: ',cam_pos)
            cv2.putText(outimage, str(blobSize), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Processed', outimage)
        cv2.imshow('Original', frame)
        
        global us_pos
        drawMap(us_pos, enc_pos, cam_pos) 

# Draws positions read from different sources on the map and then displays it.
def drawMap(us_pos=0, enc_pos=0, cam_pos=0, scale=0.5):
    img = np.copy(img_orig)
    print(us_pos)
    bluePos = int(-0.869565217 * cam_pos + 1478)   # camera
    greenPos = int(-0.869565217 * us_pos + 1478)    # ultrasonic
    redPos = int(-0.869565217 * enc_pos + 1478)   # encoders

    cv2.circle(img, (redPos,  100), int(15/scale), (0,0,255), -1)
    cv2.circle(img, (greenPos,180), int(15/scale), (0,255,0), -1)
    cv2.circle(img, (bluePos, 260), int(15/scale), (255,0,0), -1)
    cv2.putText(img, "Enc", (redPos, 100 - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.putText(img, "US",  (greenPos, 180 - 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    cv2.putText(img, "Cam", (bluePos, 260), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
    img = cv2.resize(img, (0,0), fx=scale, fy=scale)
    cv2.imshow('map',img)
    cv2.waitKey(1)


print("Battery voltage: " + str(go.volt()))

ser = serial.Serial('/dev/ttyUSB0', 9600)

lineSensorOffset = 0
try:
    _thread.start_new_thread(slowThread, ()) # Start the second thread.
    go.set_speed(60)
    ls1 = 0
    ls2 = 0
    ls3 = 0
    ls4 = 0
    ls5 = 0
    clp = 0
    dist = -1 

    # Make sure arduino is ready to send the data.
    print("Syncing serial...0%\r", end='')
    while ser.in_waiting == 0:
        ser.write("R".encode())
    print("Syncing serial...50%\r", end='')
    while ser.in_waiting > 0:
        ser.readline()
    print("Syncing serial...100%")


    '''
    This is the main thread, which should be running more important code such as
    Getting the sensor info from the serial and driving the robot.
    '''
    while True:
        # Read the serial input to string 
        ser.write("R".encode()) # Send something to the Arduino to indicate we're ready to get some data.
        serial_line = ser.readline().strip() # Read the sent data from serial.

        try:
            global us_pos
            # Decode the received JSON data
            data = json.loads(serial_line.decode())
            # Extract the sensor values
            ls1 = data['ls1']
            ls2 = data['ls2']
            ls3 = data['ls3']
            ls4 = data['ls4']
            ls5 = data['ls5']
            dist = data['us1']
            us_pos = dist
            print(dist)
        except Exception as e:  # Something went wrong extracting the JSON.
            dist = -1           # Handle the situation.
            print(e)
            pass

        if dist != -1: # If a JSON was correctly extracted, continue.
            # Print received to the console
            pass
            #print("LS1: ", ls1, "LS2: ", ls2, "LS3: ", ls3, "LS4: ", ls4, "LS5: ", ls5, "DIST: ", dist)

            # Line following logic goes here
        go.set_speed(40)
        """
        if ls4 == 0:
            go.fwd()
        """
        if ls5 == 0:
            #go.set_right_speed(45)
            #go.set_left_speed(35)
            go.right()
        elif ls3 == 0: 
            #go.set_left_speed(45)
            #go.set_right_speed(35) 
            go.left()
        else:
            #go.set_speed(40)
            go.fwd()
 
except KeyboardInterrupt:
    print("Serial closed, program finished")

finally:
    ser.close()
    running = False # Stop other threads.
go.stop() 
