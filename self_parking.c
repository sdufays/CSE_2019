#include <WMLineFollower.h>
#include <WMDMotor.h>
#include <WMMartixLed.h>
#include <WMRGBLed.h>

WMLineFollower lineFollower(11,12);
WMDMotor leftWheel(7);
WMDMotor rightWheel(8);
WMMartixLed matrixLed;
WMRGBLed rgbLED(0,0,0);

void setup() {
  matrixLed.setColorIndex(1);
  matrixLed.setBrightness(6);
  rgbLED.setColor(0,0,0);
  rgbLED.show();
}

void loop() {
  if (lineFollower.readEdgeSensor1Status()==true && lineFollower.readEdgeSensor2Status()==true){
    matrixLed.drawStr(0,0+7, "Stop");
    leftWheel.stop();
    rightWheel.stop();
    delay(5000);
  }
  else if (lineFollower.readEdgeSensor1Status()==true && lineFollower.readEdgeSensor2Status()==false){
    matrixLed.drawStr(0,0+7, "Left");
    rightWheel.run(-35);
    leftWheel.run(-10);
  }
  else if (lineFollower.readEdgeSensor1Status()==false && lineFollower.readEdgeSensor2Status()==true){
    matrixLed.drawStr(0,0+7, "Right");
    rightWheel.run(-10);
    leftWheel.run(-35);
  }
  else if (lineFollower.readEdgeSensor1Status()==false && lineFollower.readEdgeSensor2Status()==false){
    matrixLed.drawStr(0,0+7, "GO!");
    leftWheel.run(-21);
    rightWheel.run(-20);
  }
}
