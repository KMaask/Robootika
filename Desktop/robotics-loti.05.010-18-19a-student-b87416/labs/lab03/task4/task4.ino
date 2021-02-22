// Datasheet for Ultrasonic Ranging Module HC - SR04
// https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf

int echoPin = 2;
int trigPin = 3;
int delay_us = 10; // <--- YOU HAVE TO FIND THE CORRECT VALUE FROM THE DATASHEET
long distance_mm = 0;
long duration_us;

#include <Servo.h>
Servo myservo;
int pos = 0;
int dir = 0; //null kui kasvas, 1 kui kahanev


void setup()  {
  Serial.begin(9600);
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  myservo.attach(9);
  myservo.write(0);
  delay(50);
  
}

long get_distance() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(delay_us);
  digitalWrite(trigPin, LOW);

  
  duration_us = pulseIn(echoPin, HIGH);
  distance_mm = duration_us* 0.34/2;
  return distance_mm;
}

void loop() {

int dis = get_distance();

if (dis > 300) {
  if (dir==0){  
    pos +=1;
    if (pos >= 180) {
        dir = 1;
    }
  }

  else {
    pos -= 1;
    if (pos <= 0){
      dir = 0;
    }
  }
 
   myservo.write(pos);
   delay(35);
}
else {
  
  Serial.println(dis);
  }
}
