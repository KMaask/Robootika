#include <Servo.h>
Servo myservo;
int input = 0;

void setup() {
  myservo.attach(9);
  Serial.begin(9600);

}

void loop() {
  
  if (Serial.available() > 0) {
    input = Serial.parseInt();
    Serial.println(input);
    myservo.writeMicroseconds(input);
    delay(50);
  }

}
