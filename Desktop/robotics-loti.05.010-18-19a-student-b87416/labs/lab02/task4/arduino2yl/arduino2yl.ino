// defining row and column pins for ease of use.
int R1 = 2;
int R2 = 3;
int R3 = 4;
int R4 = 5;
int R5 = 6;
int R6 = 7;
int R7 = 8;
int C1 = A0;
int C2 = A1;
int C3 = A2;
int C4 = A3;
int C5 = A4;
int t = 0.5;
// the setup function runs once when you press reset or power the board
void setup() {
// setting row and column pins as output pins.
  pinMode(R1, OUTPUT);
  pinMode(R2, OUTPUT);
  pinMode(R3, OUTPUT);
  pinMode(R4, OUTPUT);
  pinMode(R5, OUTPUT);
  pinMode(R6, OUTPUT);
  pinMode(R7, OUTPUT);
  pinMode(C1, OUTPUT);
  pinMode(C2, OUTPUT);
  pinMode(C3, OUTPUT);
  pinMode(C4, OUTPUT);
  pinMode(C5, OUTPUT);

// for starters turning all the LED's off in the matrix
  digitalWrite(R1, LOW);
  digitalWrite(R2, LOW);
  digitalWrite(R3, LOW);
  digitalWrite(R4, LOW);
  digitalWrite(R5, LOW);
  digitalWrite(R6, LOW);
  digitalWrite(R7, LOW);
  digitalWrite(C1, HIGH);
  digitalWrite(C2, HIGH);
  digitalWrite(C3, HIGH);
  digitalWrite(C4, HIGH);
  digitalWrite(C5, HIGH);
 }

// the loop function runs over and over again forever

void loop() {
// turning the LED on
  digitalWrite(C1, LOW);
  digitalWrite(R3, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C1, HIGH);
  digitalWrite(R3, LOW);
  delay(t);
  
  // turning the LED on
  digitalWrite(C2, LOW);
  digitalWrite(R2, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C2, HIGH);
  digitalWrite(R2, LOW);
  delay(t);
  // turning the LED on
  digitalWrite(C3, LOW);
  digitalWrite(R1, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C3, HIGH);
  digitalWrite(R1, LOW);
  delay(t);
  
   // turning the LED on
  digitalWrite(C3, LOW);
  digitalWrite(R2, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C3, HIGH);
  digitalWrite(R3, LOW);
  delay(t);
  
   // turning the LED on
  digitalWrite(C3, LOW);
  digitalWrite(R4, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C3, HIGH);
  digitalWrite(R4, LOW);
  delay(t);
  
   // turning the LED on
  digitalWrite(C3, LOW);
  digitalWrite(R5, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C3, HIGH);
  digitalWrite(R5, LOW);
  delay(t);
  
   // turning the LED on
  digitalWrite(C3, LOW);
  digitalWrite(R6, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C3, HIGH);
  digitalWrite(R6, LOW);
  delay(t);
  
   // turning the LED on
  digitalWrite(C3, LOW);
  digitalWrite(R7, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C3, HIGH);
  digitalWrite(R7, LOW);
  delay(t);
   // turning the LED on
  digitalWrite(C4, LOW);
  digitalWrite(R2, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C4, HIGH);
  digitalWrite(R2, LOW);
  delay(t);
     // turning the LED on
  digitalWrite(C5, LOW);
  digitalWrite(R3, HIGH);
  delay(t);
  // turning the LED off
  digitalWrite(C5, HIGH);
  digitalWrite(R3, LOW);
  delay(t);
}
