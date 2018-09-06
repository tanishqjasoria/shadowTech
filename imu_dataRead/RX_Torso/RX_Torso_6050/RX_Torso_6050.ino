#include <Wire.h>
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

#define PI 3.143

long t=0,t1=0,t2=0;
long diff=0;



//IMU Variables
const int G_SENS=131;          //a division factor that directly gives omega calculated
const int MPU=0x68;                  //address of the IMU sensor

float y_old_theta=0,y_theta=0;
float x_old_theta=0,x_theta=0;
float dt=0;

int GYRY=0, GYRX=0, GYRZ=0;
float pitch = 0, roll = 0;

typedef struct
{
  int id; // id
  int pitch; // angle
  int roll;
  int gyrx;
  int gyry;
  int gyrz;
} data1;

typedef struct
{
  int id; // id
  float pitch; // angle
  float roll;
  int gyrx;
  int gyry;
  int gyrz;
} data2;

data1 temp; 
data2 thigh1 ,thigh2, knee1 ,knee2, ankle1 ,ankle2;

RF24 radio(48,53);
const uint64_t pipes[6] = { 0xF0F0F0F0E0LL ,0xF0F0F0F0E1LL, 0xF0F0F0F0E2LL, 0xF0F0F0F0E3LL ,0xF0F0F0F0E4LL ,0xF0F0F0F0E5LL };


void setup(void) {
  t=millis();
  Serial.begin(115200);
  Serial3.begin(57600);
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
  print_shadow();
} 

void print_shadow()
{
 Serial.print(thigh1.pitch);Serial.print(",");
 Serial.print(thigh2.pitch);Serial.print(",");
 Serial.print(knee1.pitch);Serial.print(",");
 Serial.println(knee2.pitch);
}  
void _print()
{
 Serial.print("t1: ");Serial.print(" pit=");Serial.print(thigh1.roll);Serial.print(" roll=");Serial.print(thigh1.roll);  
 Serial.print("  t2: ");Serial.print(" pit=");Serial.print(thigh2.roll);Serial.print(" roll=");Serial.print(thigh2.roll);
 Serial.print("  k1: ");Serial.print(" pit=");Serial.print(knee1.roll);Serial.print(" roll=");Serial.print(knee1.roll);
 Serial.print("  k2: ");Serial.print(" pit=");Serial.print(knee2.roll);Serial.print(" roll=");Serial.print(knee2.roll);
 //Serial.print("  a1: ");Serial.print(" pit=");Serial.print(ankle1.pitch);Serial.print(" roll=");Serial.print(ankle1.roll);Serial.print("\tF1 =");Serial.print(ankle1.forceSens6);Serial.print("\tF2 =");Serial.print(ankle1.forceSens7);Serial.print("\tF3 =");Serial.println(ankle1.forceSens8);//Serial.print("\tF4 =");Serial.print(Data.forceSens4);Serial.print("\tF5 =");Serial.println(Data.forceSens5);
 //Serial.print("  a2: ");Serial.print(" pit=");Serial.print(ankle2.pitch);Serial.print(" roll=");Serial.print(ankle2.roll);Serial.print("\tF1 =");Serial.print(ankle2.forceSens6);Serial.print("\tF2 =");Serial.print(ankle2.forceSens7);Serial.print("\tF3 =");Serial.print(ankle2.forceSens8);//Serial.print("\tF4 =");Serial.print(ankle2.forceSens4);Serial.print("\tF5 =");Serial.println(ankle2.forceSens5);
 Serial.print("  T: ");Serial.print(" pit=");Serial.print(pitch);Serial.print(" roll=");Serial.print(roll);Serial.print("  time");Serial.println(diff);
 Serial.println();
}
