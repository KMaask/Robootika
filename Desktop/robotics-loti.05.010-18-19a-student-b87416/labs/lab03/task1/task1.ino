void setup()  {
  Serial.begin(9600);
  Serial.println("Hello!");
  Serial.println("Please enter a number and press ENTER.");
}
void loop() {
  // YOUR CODE GOES HERE
  if (Serial.available() > 0) {
    //int inByte = Serial.read();
    //Serial.print(inByte, DEC);
    long nr = Serial.parseInt();
    Serial.println(nr);
    if (nr > 300) {
      Serial.print("GO");
    }
    else {
      Serial.print("STOP");
    }
  }

}
