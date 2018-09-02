import serial
import time
from roboclaw import Roboclaw
import invK
port1 = ""
port2 = ""
address = 0x80

def initOutput(outputFile)
	file = open(outputFile, "r+")
	print "Name of the file: ", fo.name
	print "Closed or not : ", fo.closed
	print "Opening mode : ", fo.mode
	print "Softspace flag : ", fo.softspace
	return file


def roboclawInit(port1, port2):
	rc1 = Roboclaw(port1 ,115200)
	rc2 = Roboclaw(port2 ,115200)
	rc1.Open()
	rc2.Open()
	rc1.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
	rc1.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)
	rc2.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
	rc2.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)


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

def arduinoRead(port, Data):
	box = serial.Serial(port, 115200)
	while True:
	        x=box.read()
	        x.strip()
	        print(x)
	        try:
		        data = x.split(',')
		        t1 = data[0]
		        t2 = data[1]
		        k1 = data[2]
		        k2 = data[3]
		    except:
		    	print("This Line not processed")
		    	continue
		    t1 = getLeftHip(t1)
		    t2 = getRightHip(t2)
		    k1 = getLeftKnee(k1)
		    k2 = getRightKnee(k2)
		    try:
			    rc1.SpeedAccelDeccelPositionM1(address,0,0,0,int(-(k2/360)*2000),0)
				rc1.SpeedAccelDeccelPositionM2(address,0,0,0,int(-(t2/360)*2000),0)
				rc2.SpeedAccelDeccelPositionM1(address,0,0,0,int((t1/360)*2000),0)
				rc2.SpeedAccelDeccelPositionM2(address,0,0,0,int((k1/360)*2000),0)
			except:
				print("Error rotating motor")
