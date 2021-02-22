int lightPin = A0;
int ledPin = 9;
int light = 0;
int ledValue = analogRead(0);
int t = 0;

void setup() {
  Serial.begin(9600);
  pinMode(lightPin, INPUT);
}

void loop() {
  light = analogRead(lightPin);
  Serial.println(light, DEC);

  if ((light) >= 250) {
    ledValue = 0;
    analogWrite(ledPin, ledValue);
    delay(t);
  }
  else if ((light) < 250 and (light) > 30) {
    ledValue = map(ledValue, 10, 150, 30, 250);
    analogWrite(ledPin, ledValue);
    delay(t);
  }
  else if ((light) < 30) {
    ledValue = 255;
    analogWrite(ledPin, ledValue);
    delay(t);
  }

}
