#include <Wire.h>
#include <Servo.h>
#include <LSM303.h>
LSM303 compass;
Servo myservo;
char report[80];

void setup() {
  Serial.begin(9600);
  Wire.begin();
  compass.init();
  compass.enableDefault();
  myservo.attach(9);
}

void loop() {
  
  compass.read();
  myservo.writeMicroseconds((compass.a.z) *0.01+1500);
  delay(30);

}
