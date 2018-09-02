import serial

def arduinoRead(port, Data):
	box = serial.Serial(port, 115200)
	while True:
	        x=box.read()
	        print(x)
	        data = x.split(',')


