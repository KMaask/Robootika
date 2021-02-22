#include <Wire.h>
#include <LPS.h>
#include <L3G.h>
#include <LSM303.h>
L3G gyro;
LPS ps;
LSM303 compass;


char report[80];

void setup() {
  Serial.begin(9600);
  Wire.begin();
  gyro.enableDefault();
  compass.enableDefault();
  ps.enableDefault();
}

void loop() {
  float pressure = ps.readPressureMillibars();
  float altitude = ps.pressureToAltitudeMeters(pressure);
  float temperature = ps.readTemperatureC();
  gyro.read();

  Serial.print("G ");
  Serial.print("X: ");
  Serial.print((int)gyro.g.x * 0.00875);
  Serial.print(" Y: ");
  Serial.print((int)gyro.g.y * 0.00875); 
  Serial.print(" Z: ");
  Serial.println((int)gyro.g.z * 0.00875);
  Serial.print("dps\ta:");

  delay(100);

  compass.read();
  Serial.print("Kompass");
  Serial.print((compass.a.x) * 0.00160));
  Serial.print("gauss\ta: ");
  Serial.print("Kompass");
  Serial.print((compass.a.y) * 0.00160));
  Serial.print("gauss\ta: ");
  Serial.print("Kompass");
  Serial.print((compass.a.z) * 0.00160));
  Serial.print("gauss\ta: ");
  Serial.print("Kompass");


  Serial.print("g");
  Serial.print((compass.a.x * 0.061) / 1000);
  Serial.print("g-units\ta: ");
  delay(100);

  Serial.print("p: ");
  Serial.print(pressure);
  Serial.print(" mbar\ta: ");
  Serial.print(temperature);
  Serial.println(" °C");

  delay(100);

}
