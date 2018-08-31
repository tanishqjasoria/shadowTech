#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

long t=0,t1=0,t2=0;
long diff=0;

typedef struct
{
  int id; // id
  float pitch; // angle
  float roll;
  int gyrx;
  int gyry;
  int gyrz;
} data;

data thigh1 ,thigh2, knee1 ,knee2, ankle1 ,ankle2 ,temp;

RF24 radio(48,53);
const uint64_t pipes[6] = { 0xF0F0F0F0E0LL ,0xF0F0F0F0E1LL, 0xF0F0F0F0E2LL, 0xF0F0F0F0E3LL ,0xF0F0F0F0E4LL ,0xF0F0F0F0E5LL };

void setup(void) {
  t=millis();
Serial.begin(115200);

radio.begin();
radio.setDataRate(RF24_2MBPS);
radio.setPALevel(RF24_PA_MIN);

radio.openReadingPipe(0, pipes[0]);
radio.openReadingPipe(1, pipes[1]);
radio.openReadingPipe(2, pipes[2]);
radio.openReadingPipe(3, pipes[3]);
radio.openReadingPipe(4, pipes[4]);
radio.openReadingPipe(5, pipes[5]);

//radio.closeReadingPipe(pipes[1]);

radio.startListening();
}

void loop(void)
{
  
  if ( radio.available() )
  {
    //Serial.println("Hello");
    //delay(5);
    radio.read(&temp, sizeof(temp));
    
    switch(temp.id)
    {
      case 0:
      thigh1.id=0;
      thigh1.pitch = ((float)temp.pitch)/100.0;
      thigh1.roll = ((float)temp.roll)/100.0;
      thigh1.gyrx = temp.gyrx;
      thigh1.gyry = temp.gyry;
      thigh1.gyrz = temp.gyrz;
      break;
      
      case 1:
      thigh2.id=1;
      thigh2.pitch = ((float)temp.pitch)/100;
      thigh2.roll = ((float)temp.roll)/100;
      thigh2.gyrx = temp.gyrx;
      thigh2.gyry = temp.gyry;
      thigh2.gyrz = temp.gyrz;
      break;
      
      case 2:
      knee1.id=0;
      knee1.pitch = ((float)temp.pitch)/100;
      knee1.roll = ((float)temp.roll)/100;
      knee1.gyrx = temp.gyrx;
      knee1.gyry = temp.gyry;
      knee1.gyrz = temp.gyrz;
      break;
      
      case 3:
      knee2.id=0;
      knee2.pitch = ((float)temp.pitch)/100;
      knee2.roll = ((float)temp.roll)/100;
      knee2.gyrx = temp.gyrx;
      knee2.gyry = temp.gyry;
      knee2.gyrz = temp.gyrz;
      break;
      
      case 4:
      ankle1.id=4;
      ankle1.pitch = ((float)temp.pitch)/100;
      ankle1.roll = ((float)temp.roll)/100;
      ankle1.gyrx = temp.gyrx;
      ankle1.gyry = temp.gyry;
      ankle1.gyrz = temp.gyrz;
      break;
      
      case 5:
      ankle2.id=5;
      ankle2.pitch = ((float)temp.pitch)/100;
      ankle2.roll = ((float)temp.roll)/100;
      ankle2.gyrx = temp.gyrx;
      ankle2.gyry = temp.gyry;
      ankle2.gyrz = temp.gyrz;
      break;
      default:
      break;  
    }  
  }
  else
  {
    //Serial.println("no data available");
  }
 
 t1=millis();
 diff=t1-t2;
 t2=t1;
  _print();
} 


void _print()
{
 Serial.print(thigh1.pitch);Serial.print(" ");Serial.print(thigh1.roll);Serial.print(" ");
 Serial.print(thigh2.pitch);Serial.print(" ");Serial.print(thigh2.roll);Serial.print(" ");
 Serial.print(knee1.pitch);Serial.print(" ");Serial.print(knee1.roll);Serial.print(" ");
 Serial.print(knee2.pitch);Serial.print(" ");Serial.print(knee2.roll);Serial.print(" ");
 Serial.println(diff);
}
