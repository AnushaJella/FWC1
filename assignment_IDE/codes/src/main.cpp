#include<Arduino.h>
//Declaring all variables as integers
//int Z=0,W=0,V=0,U=1;
int A,B,C;
int F;

//}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);  
  
   pinMode(5, INPUT);  
   pinMode(6, INPUT);
   pinMode(7, INPUT);
  
    
}

// the loop function runs over and over again forever
void loop() {
  
A= digitalRead(5);//LSB  
B = digitalRead(6);  
C = digitalRead(7);//MSB  
F=(!B && !C) || (B && C);
  
digitalWrite(2,F);
}
