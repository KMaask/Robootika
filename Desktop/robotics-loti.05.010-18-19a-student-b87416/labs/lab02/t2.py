# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# reference pins by GPIO numbers
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)

# define row and column pin numbers
row_pins = [25, 8, 7, 12, 16, 20, 21]
col_pins = [5, 6, 13, 19, 26]

# set all the pins as outputs and set column pins high, row pins low
GPIO.setup(col_pins, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(row_pins, GPIO.OUT, initial=GPIO.LOW)

# Sets the waiting time between rows. With larger wait times (0.1) you can see that rows are lit up at different times. With smaller times (0.01) the LEDs appear to be not blinking at all
wait_time = 0.001


 # sets column number 3 low)
while True:
 
  GPIO.output(row_pins[0], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[0], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)


  GPIO.output(row_pins[1], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[1], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)

  GPIO.output(row_pins[2], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[2], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)

  GPIO.output(row_pins[3], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[3], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)

  GPIO.output(row_pins[4], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[4], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)

  GPIO.output(row_pins[5], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[5], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)


  GPIO.output(row_pins[6], GPIO.HIGH)
  GPIO.output(col_pins[2], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[6], GPIO.LOW)
  GPIO.output(col_pins[2], GPIO.HIGH)

  GPIO.output(row_pins[1], GPIO.HIGH)
  GPIO.output(col_pins[1], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[1], GPIO.LOW)
  GPIO.output(col_pins[1], GPIO.HIGH)

  GPIO.output(row_pins[2], GPIO.HIGH)
  GPIO.output(col_pins[0], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[2], GPIO.LOW)
  GPIO.output(col_pins[0], GPIO.HIGH)

  GPIO.output(row_pins[1], GPIO.HIGH)
  GPIO.output(col_pins[3], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[1], GPIO.LOW)
  GPIO.output(col_pins[3], GPIO.HIGH)

  GPIO.output(row_pins[2], GPIO.HIGH)
  GPIO.output(col_pins[4], GPIO.LOW)
  time.sleep(wait_time)
  GPIO.output(row_pins[2], GPIO.LOW)
  GPIO.output(col_pins[4], GPIO.HIGH)



# reset GPIO
GPIO.cleanup()

