import Adafruit_CharLCD as LCD
import os
import datetime
import commands
import time
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

# Return device IP as a character string

def getIP():
	return commands.getoutput('hostname -I')
def getTimeText():
        t = datetime.datetime.now()
        hours = str(t.hour)
        minutes = str(t.minute)
        seconds = str(t.second)
        timetext = hours + ':' + minutes + ':' + seconds
        return timetext

lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_color(0, 1, 0)

while True:
	if lcd.is_pressed(LCD.LEFT):
		lcd.clear()
		lcd.message(getCPUtemperature())
		time.sleep(0.5)
	elif lcd.is_pressed(LCD.UP):
		lcd.clear()
		lcd.message('IP:'+ getIP())
		time.sleep(0.5)
	elif lcd.is_pressed(LCD.RIGHT):
		lcd.clear()
		lcd.message(getTimeText())
		time.sleep(0.5)
	elif lcd.is_pressed(LCD.SELECT):
		lcd.clear()
		lcd.message(getTimeText()+"\n"+getCPUtemperature())
		time.sleep(0.5)



