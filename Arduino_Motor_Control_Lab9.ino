
#include<Servo.h>
//Motors
Servo Servo1;   
Servo Servo2;

//Varriables
int Signal;
int Servo1_Position, Servo2_Position;

void setup() {
  Serial.begin(9600);
  Servo1.attach(8);
  Servo2.attach(7);

  Servo1.write(90);
  Servo2.write(90);

}

void loop() {
  if (Serial.available() > 0){                      //checks for values on the serial
    String Signal = Serial.readStringUntil('\n');
    
    if(Signal == "M1"){
      String Signal = Serial.readStringUntil('\n');
      Servo1_Position = Signal.toInt() + 90;
      Servo1.write(Servo1_Position);
    }
    
    else if(Signal == "M2"){
      String Signal = Serial.readStringUntil('\n');
      Servo2_Position = Signal.toInt() + 90;
      Servo2.write(Servo2_Position);
    }
  }

}
