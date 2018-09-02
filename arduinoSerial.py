import serial

def arduinoRead(port):
	ser = serial.Serial(port, 115200)
	text_file = open("test_data.txt",'w')
	while True:
	        x=ser.read()
	        print(x),
	        text_file.write(x)
	        text_file.flush()
