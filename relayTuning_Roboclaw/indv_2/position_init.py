#***Before using this example the motor/controller combination must be
#***tuned and the settings saved to the Roboclaw using IonMotion.
#***The Min and Max Positions must be at least 0 and 50000

import time
from roboclaw import Roboclaw


#Windows comport name
#rc = Roboclaw("COM3",115200)
#Linux comport name
rc = Roboclaw("/dev/ttyACM0",115200)
f=open("final.csv.txt","w+")

def displayspeed(ti):
	enc1 = rc.ReadEncM1(address)
	enc2 = rc.ReadEncM2(address)
	speed1 = rc.ReadSpeedM1(address)
	speed2 = rc.ReadSpeedM2(address)
	f.write(str(ti)+",")
	print("Encoder1:"),
	if(enc1[0]==1):
		print enc1[1],
		print format(enc1[2],'02x'),
		f.write(str(enc1[1]*0.18))
		f.write(",")
	else:
		print "failed",
	print "Encoder2:",
	if(enc2[0]==1):
		print enc2[1],
		print format(enc2[2],'02x'),
		f.write(str(enc2[1]*0.18))
		f.write("\n")
	else:
		print "failed " ,
	print "Speed1:",
	if(speed1[0]):
		print speed1[1],
	else:
		print "failed",
	print("Speed2:"),
	if(speed2[0]):
		print speed2[1]
	else:
		print "failed "

rc.Open()
address = 0x80



#Open a file
fo = open("data_init.txt", "r+")

print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

j=0
data=""
i=0
motor_data=[]
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
rc.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
rc.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)
time.sleep(1)

init_time=time.clock();
while True:


    chunk = fo.readline()
    if chunk == '':
        break
    else :
		#print "Data is :",chunk
		for j in range(0,len(chunk)):
			
			if(chunk[j]==','):
				motor_data[i]=float(data)
				data=""
				i=i+1
				if(i==5):
					break
			else:
				data=data+chunk[j]	

			#print "D",chunk[j]

	 	print "Time_Data",motor_data[0]
	 	print "Motor 1",motor_data[3]
		print "Motor 2",motor_data[4]
		#print (motor_data[3])
		#print (motor_data[4])
		i=0
		while((time.clock()-init_time)<=motor_data[0]):
			{

			}
		
		rc.SpeedAccelDeccelPositionM1(address,0,0,0,int(-(motor_data[3]/360)*2000),0)
		rc.SpeedAccelDeccelPositionM2(address,0,0,0,int(-(motor_data[4]/360)*2000),0)
		displayspeed(time.clock()-init_time)
		print "Time_Actual",(time.clock()-init_time)



'''
while(1):
	print "Pos 50000"
	rc.SpeedAccelDeccelPositionM2(address,0,0,0,2000,0)
	
	time.sleep(2)
	
	print "Pos 0"
	rc.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)
	
  
  	time.sleep(2)

	print "Pos 50000"
	rc.SpeedAccelDeccelPositionM1(address,0,0,0,2000,0)
	
	time.sleep(2)
	
	print "Pos 0"
	rc.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
	
  
  	time.sleep(2)

'''