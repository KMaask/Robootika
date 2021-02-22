
const int pirPin = 5;
// passive infrared sensor pin
int state = 0;
int ledPin = 3;
unsigned long time; // algusaeg
// 0 - no motion, 1 - motion detected
int ledstate = LOW;

void setup() {
  Serial.begin(9600);         // initialize serial with 9600 baud rate
  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);     // set pin #5 as an input from PIR
  time = millis();
}

void loop() {

  if (digitalRead(pirPin) == HIGH  &&  state == 0) {
    Serial.println("Motion detected!");
    state = 1;

   
  }
  if (digitalRead(pirPin) == LOW  &&  state == 1) {
    Serial.println("No movement anymore");
    state = 0;
   



  }
  if (state == 1) {
    if (millis() - time >= 100) {
      time = millis();
      if (ledstate == LOW) {
        ledstate = HIGH;

      }
      else {
        ledstate = LOW;
      }
      digitalWrite(ledPin, ledstate);
    }




  }
}
