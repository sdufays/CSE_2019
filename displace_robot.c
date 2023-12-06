#include <Arduino.h>
#include <WMHead.h>
#include <WMBoard.h>

WMRGBLed rgbLED(0, 4);
WMMartixLed matrixLed(5);
WMDMotor m1(7);
WMDMotor m2(8);

void moveForward() {
  matrixLed.drawStr(0, 0+7, "Go");
  delay(2500);
  m1.run(-50.6);
  m2.run(-50);
  delay(1440);
  m1.stop();
  m2.stop();
  delay(1500);
}

void turnRightmoveForward() {
  m2.run(-50);
  delay(700);
  m1.run(-50);
  m2.run(-50);
  delay(1950);
  m1.stop();
  m2.stop();
  delay(1500);
}

void turnLeftmoveForward() {
  m1.run(-50);
  delay(600);
  m1.run(-50);
  m2.run(-50);
  delay(750);
  m1.stop();
  m2.stop();
  delay(1500);
}

void moveForward2() {
  matrixLed.drawStr(0, 0+7, "Go");
  m1.run(-50.6);
  m2.run(-50);
  delay(810);
  m1.run(-50.6);
  m2.run(-50);
  delay(1600);
  m1.stop();
  m2.stop();
}

void turnLeft() {
  m1.run(-50);
  delay(600);
  m1.run(-50);
  m2.run(-50);
  delay(1950);
  m1.stop();
  m2.stop();
}

void setup() {
  moveForward();
  turnRightmoveForward();
  turnLeftmoveForward();
  moveForward2();
  turnLeft();
}

void loop() {
  // Empty loop
}
