#include <Servo.h>
#include <SoftwareSerial.h>

Servo myservo;
int on = 78;
int off = 105;
int c = 0;
int btnpin=12;
char blue_in='a';
int bt_txd=2;
char serialData;
int bt_rxd=3;
SoftwareSerial bluetooth(bt_txd,bt_rxd);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  bluetooth.begin(9600);
  myservo.attach(10);
  pinMode(btnpin,INPUT_PULLUP);
  
}
void loop() {
  if (digitalRead(btnpin)==1){
    if (c==0){
      myservo.write(on);
      Serial.print("on\n");
      delay(200);
      c=1;
    }
    else if (c==1){
      myservo.write(off);
      Serial.print("off\n");
      delay(200);
      c=0;
    }
  }
  if (bluetooth.available()){
    blue_in=bluetooth.read();
    if (blue_in == '0'){
      myservo.write(on);
      Serial.print("on\n");
      delay(1);
      c=1;
    }
    else if (blue_in == '1'){
      myservo.write(off);
      Serial.print("off\n");
      delay(1);
      c=0;
    }
  }
  if (Serial.available()>0){
    serialData = Serial.read();
    if (serialData=='1'){
      myservo.write(off);
      delay(1);
      c=0;
    }
    else if (serialData=='0'){
      myservo.write(on);
      delay(1);
      c=1;
    }
  }

  delay(1);
}
