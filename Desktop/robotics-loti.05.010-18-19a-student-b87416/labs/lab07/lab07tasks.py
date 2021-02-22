# -*- coding: utf-8 -*-
import gopigo as go
from gopigo import*
import numpy as np
import cv2
from time import time
import math

# global variable for determining gopigo speed
gospeed = 100


lH = 154
lS = 89
lV = 0
hH = 255
hS = 140
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

# global variable for video feed
cap = None

def init():
    global cap, gospeed
    # This function should do everything required to initialize the robot.
    # Among other things it should open the camera and set gopigo speed.
    # Some of this has already been filled in.
    # You are welcome to add your own code, if needed.
    
    cap = cv2.VideoCapture(0)
    go.set_speed(gospeed)
    return cap


# TASK 1
def get_line_location(frame):
    
    lowerLimits = np.array([lH, lS, lV])
    upperLimits = np.array([hH, hS, hV])

    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    cv2.imshow('Thresholded', thresholded)
    pikslid = np.nonzero(thresholded)
    keskmine = np.mean(pikslid[1])
    
    # This function should use frame from camera to determine line location.
    # It should return location of the line in the frame.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE
    if math.isnan(keskmine):
        keskmine = 0
    print(keskmine)
    return int(keskmine)
    

# TASK 2
def bang_bang(linelocation):
    # This function should use the line location to implement a simple bang-bang controller.
    # YOUR CODE HERE    
    kaadrik = len(frame[0])/2
    if linelocation >= kaadrik:
        go.set_right_speed(gospeed)
        go.set_left_speed(gospeed+10)
        go.fwd()
    elif linelocation <= kaadrik:
        go.set_right_speed(gospeed+10)
        go.set_left_speed(gospeed)
        go.fwd()
        
    else:
        go.set_right_speed(gospeed)
        go.set_left_speed(gospeed)
        go.fwd()
    


# TASK 3
def bang_bang_with_hysteresis(linelocation):
    # This function should use the line location to implement bang-bang controller with hysteresis.
    # YOUR CODE HERE
    kaadrik = len(frame[0])/2
    if linelocation >= kaadrik+20:
        go.set_right_speed(gospeed)
        go.set_left_speed(gospeed+20)
        go.fwd()
    elif linelocation <= kaadrik-20:
        go.set_right_speed(gospeed+20)
        go.set_left_speed(gospeed)
        go.fwd()
        
    else:
        go.set_right_speed(gospeed)
        go.set_left_speed(gospeed)
        go.fwd()
    
    
    return


# TASK 4
def proportional_controller(linelocation):
    # This function should use the line location to implement proportional controller.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE
    kaadrik = len(frame[0])/2
    e = kaadrik - int(linelocation)
    p = int(0.12*e)
    
    if linelocation == 0:
        go.set_right_speed(gospeed-p)
        go.set_left_speed(gospeed+p)
        go.fwd()
        
    if linelocation > 500:
        go.set_right_speed(gospeed+p)
        go.set_left_speed(gospeed-p)
        go.fwd()
        
    elif linelocation < 250:
        go.set_right_speed(gospeed-p)
        go.set_left_speed(gospeed+p)
        go.fwd()
        
    else:
        go.set_right_speed(gospeed)
        go.set_left_speed(gospeed)
        go.fwd()
    return

aeg = time()
eelmine_e = 0
errors = 0
Tu = 2.6
Ku = 0.03
Kp = 0.6*Ku
#Kp = 0
#Ki = 0
#Kd = 0
Ki = (1.2*Ku)/Tu
Kd = (3*Ku*Tu)/40
# TASK 5
def pid_controller(linelocation):
    # This function should use the line location to implement PID controller.
    # Feel free to define and use any global variables you may need.
    # YOUR CODE HERE
    global eelmine_e, errors, aeg
    dt = time() - aeg
    aeg = time()
    hetke_e = 320 - linelocation
    errors = (errors + hetke_e)*dt
    d = (hetke_e - eelmine_e)/dt
    u = int(Kp*hetke_e + Ki *errors + Kd* d)

    go.set_right_speed(gospeed + u)
    go.set_left_speed(gospeed - u)
    go.fwd()
        
    print(dt)


    return


# Initialization
init()
tulem = ''
while True:
    # We read information from camera.
    start = time()
    ret, frame = cap.read()
    r = [len(frame)-178, len(frame)-170, 0, len(frame[0])]
    frame=frame[r[0]:r[1], r[2]:r[3]]

    cv2.putText(frame, tulem, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Original', frame)
    # Task 1: uncomment the following line and implement get_line_location function.
    linelocation = get_line_location(frame)
    
    # Task 2: uncomment the following line and implement bang_bang function.
    #bang_bang(linelocation)
    
    # Task 3: uncomment the following line and implement bang_bang_with_hysteresis function.
    #bang_bang_with_hysteresis(linelocation)
    
    # Task 4: uncommment the following line and implement proportional_controller function.
    #proportional_controller(linelocation)

    
    # Task 5: uncomment the following line and implement pid_controller function.
    pid_controller(linelocation)
    lopp = time()
    tulem = str(round(1/(lopp - start), 2))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        go.stop()
        break

cap.release()
cv2.destroyAllWindows()
go.stop()
