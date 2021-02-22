#include <Servo.h>
Servo myservo;


void setup() {
myservo.attach(9);
myservo.writeMicroseconds(1500);
delay(3000);

myservo.writeMicroseconds(1400);
delay(2000);


myservo.writeMicroseconds(1490);
delay(2000);


myservo.writeMicroseconds(1600);
delay(2000);


myservo.writeMicroseconds(1510);
delay(2000);
myservo.writeMicroseconds(1500);





}

void loop() {
  // put your main code here, to run repeatedly:

}
