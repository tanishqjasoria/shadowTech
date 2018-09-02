import time
from roboclaw import Roboclaw

rc1 = Roboclaw("/dev/ttyACM0",115200)
rc2 = Roboclaw("/dev/ttyACM1",115200)

f1 = open("a_Data1.csv","w+")


def displayspeed1(ti1):
	enc1 = rc1.ReadEncM1(address)
	enc2 = rc1.ReadEncM2(address)
	enc3 = rc2.ReadEncM1(address)
	enc4 = rc2.ReadEncM2(address)

	f1.write(str(ti1)+",")
	print("Encoder1:"),
	if(enc1[0]==1):
		print enc1[1],
		print format(enc1[2],'02x'),
		f1.write(str(enc1[1]*0.18))
		f1.write(",")
	else:
		print "failed",
	print "Encoder2:",
	if(enc2[0]==1):
		print enc2[1],
		print format(enc2[2],'02x'),
		f1.write(str(enc2[1]*0.18))
		f1.write(",")
	else:
		print "failed " ,
	print("Encoder3:"),
	if(enc3[0]==1):
		print enc3[1],
		print format(enc3[2],'02x'),
		f1.write(str(enc3[1]*0.18))
		f1.write(",")
	else:
		print "failed",
	print "Encoder4:",
	if(enc4[0]==1):
		print enc4[1],
		print format(enc4[2],'02x'),
		f1.write(str(enc4[1]*0.18))
		f1.write("\n")
	else:
		print "failed " ,
	

rc1.Open()
rc2.Open()
address = 0x80

fo = open("m_data.txt", "r+")

print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

j=0
i=0
motor_data=[]
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
motor_data.append(0)
rc1.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
rc1.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)
rc2.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
rc2.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)
data=""
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

	 	#print "Time_Data",motor_data[0]
	 	#print "Motor 1",motor_data[1]
		#print "Motor 2",motor_data[2]
		#print (motor_data[3])
		#print (motor_data[4])
		i=0
		while((time.clock()-init_time)<=motor_data[0]):
			{

			}
		
		rc1.SpeedAccelDeccelPositionM1(address,0,0,0,int(-(motor_data[1]/360)*2000),0)
		rc1.SpeedAccelDeccelPositionM2(address,0,0,0,int(-(motor_data[2]/360)*2000),0)
		rc2.SpeedAccelDeccelPositionM1(address,0,0,0,int((motor_data[3]/360)*2000),0)
		rc2.SpeedAccelDeccelPositionM2(address,0,0,0,int((motor_data[4]/360)*2000),0)

		displayspeed1(time.clock()-init_time)
		print "Time_Actual",(time.clock()-init_time)
