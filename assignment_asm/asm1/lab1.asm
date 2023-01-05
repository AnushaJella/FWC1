.include "/home/anu_krishna/m328Pdef.inc"

ldi r16,0b00000100  ;2 pins
out DDRD,r16

ldi r17, 0b11111000 ; identifying input pins 8,9,10
	out DDRB,r17		; declaring pins as input
ldi r17, 0b11111110 ;
	out PORTB,r17		; activating internal pullup for pins 8,9,10 

ldi r18,0b00000001 ; value
ldi r19,0b00000001 ; value
ldi r20,0b00000001; value


;in r17,PINB

and r18,r17 ; C
lsr r17;
and r19,r17;B
lsr r17;
and r20,r17; A
lsr r17;

ldi r21,0b00000001;
eor r21,r18;  C'
ldi r22,0b00000001;
eor r22,r19; B'
ldi r23,0b00000001;
eor r23,r20; A'

ldi r16,0b00000000;
mov r16,r18   ;for C
and r16,r19;  B C
ldi r24,0b00000000;
mov r24,r21;
and r24,r22;  B C 
or r16,r24;
lsl r16      ;
lsl r16;


out PORTD,r16             ;F output

start:
rjmp start

