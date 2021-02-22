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
  gyro.init();
  gyro.enableDefault();
  compass.init();
  compass.enableDefault();
  ps.init();
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
  Serial.print((int)gyro.g.z * 0.00875);
  Serial.println("dps\ta:");

  delay(1000);
  Serial.print("\t");
  compass.read();
  Serial.print((compass.a.x) * 0.00160);
  Serial.print("gauss\ta: ");
  Serial.print((compass.a.y) * 0.00160);
  Serial.print("gauss\ta: ");
  Serial.print((compass.a.z) * 0.00160);
  Serial.print("gauss\ta: ");



  Serial.print("g");
  Serial.print((compass.a.x * 0.061) / 1000);
  Serial.print("g-units\ta: ");
  Serial.print((compass.a.y * 0.061) / 1000);
  Serial.print("g-units\ta: ");
  Serial.print((compass.a.z * 0.061) / 1000);
  Serial.println("g-units\ta: ");

  Serial.print("p: ");
  Serial.print(pressure);
  Serial.print(" \t mbar\t");
  Serial.print("H: ");
  Serial.print(altitude);
  Serial.print(" m\tt: ");
  Serial.print(temperature);
  Serial.println(" °C");

  delay(1000);

}
