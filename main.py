import serial
import time
from roboclaw import Roboclaw
import invK as inv
port1 = ""
port2 = '/dev/ttyACM1'
address = 0x80
port = '/dev/ttyACM2'
t10 = 0
k10 = 0
beta = 0.2
outputFile = "data.txt"
"""def initOutput()
    
    print "Name of the file: ", fo.name
    print "Closed or not : ", fo.closed
    print "Opening mode : ", fo.mode
    print "Softspace flag : ", fo.softspace
    return file"""


"""def displayspeed1(ti1):
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
"""

def arduinoRead(port,port2):
    f = open(outputFile, "r+")
    rc = Roboclaw(port2 ,115200)
    rc.Open()
    rc.SpeedAccelDeccelPositionM1(address,0,0,0,0,0)
    rc.SpeedAccelDeccelPositionM2(address,0,0,0,0,0)
    t10 = 0
    k10 = 0
    box = serial.Serial(port, 115200)
    while True:
        x=box.readline()
        try:
            x = x.decode("utf-8")
            #print("Input")
           # print(x)
            #print("input end")
            data = x.split(',')
            t1 = float(data[0])
            t2 = float(data[1])
            k1 = float(data[2])
            k2 = float(data[3])
            #print("INDV")
            print(t1),
            print(t2),
            print(k1),
            print(k2)
            #print("indv end")
        except:
            print("This Line not processed")
            continue
        try:
            t2 = 89
            k2 = 89
            t1 = inv.getLeftHip(t1) - 544.7462849003102
        except:
            print("t1")
        try:
            t2 = inv.getRightHip(t2) - 544.7462849003102
            k1 = inv.getLeftKnee(k1) - 288.5185921120647
            k2 = inv.getRightKnee(k2) - 288.5185921120647

        except:
            print("k1")
            continue
        #print("INVK")
        f.write(str(t1))
        f.write(',')
        f.write(str(k1))
        f.write('\n')
        print(t1),
        print(t2),
        print(k1),
        print(k2)
        #print("invk end")
        try:
            #rc1.SpeedAccelDeccelPositionM1(address,0,0,0,int(-(k2/360)*2000),0)
            #rc1.SpeedAccelDeccelPositionM2(address,0,0,0,int(-(t2/360)*2000),0)
            rc.SpeedAccelDeccelPositionM1(address,0,0,0,-int((t1/360)*2000),0)
            rc.SpeedAccelDeccelPositionM2(address,0,0,0,-int((k1/360)*2000),0)
        except:
            print("Error rotating motor")

arduinoRead(port,port2)
