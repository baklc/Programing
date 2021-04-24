#include <Servo.h>

Servo servo;
Servo esc;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  servo.attach(10);
  esc.attach(8);
  esc.write(70);
  delay(1000);
}

String readSerial()   
{   
   String str = "";   
   char ch;   
    while( Serial.available() > 0 )   
    {   
      ch = Serial.read();  
      str.concat(ch);   
      delay(10);  
    }   
    return str;     
}   

void loop() {

  String a=readSerial();
  int l=a.length();
  char c=a.charAt(0);
  String n=a.substring(1,l);
  int d=n.toInt();
  
  if (c=='s'){
    servo.write(d);
  }
  else if (c=='e'){
      esc.write(d);
  }
  else if (c=='l'){
      if (d==1){
          digitalWrite(7,HIGH);
          digitalWrite(6,HIGH);
      }
      else if (d==2){
          digitalWrite(7,LOW);
          digitalWrite(6,LOW);
      }

  }
  delay(1);
  
}