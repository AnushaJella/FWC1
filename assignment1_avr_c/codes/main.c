//Takes ABC number as input and print boolean expression F=B'C'+BC as output

#include <avr/io.h>

#include <util/delay.h>

#include <stdbool.h>


int main (void)

{

 bool U,V,F;

 bool A=1,B=1,C=0;

 DDRD = 0b00000100;

 DDRB = 0b00100000;

 PORTD = 0b11000000;

 PORTB = 0b00000011;

        while(1){

// PORTB = ((1 <<  PB5));

 //_delay_ms (200L);

  U=(!B && !C);

  V=(B && C);

  F=U || V;
  PORTD = (F << 2);
 //PORTB = ((0 <<  PB5));

   //_delay_ms (200L);

 }

        return 0;

}
