#!/usr/bin/env python
import time
import serial
import sys
#hola 2
#hola 
ser = serial.Serial('/dev/ttyAMA0',
 9600,
 timeout = 0,
 bytesize = serial.EIGHTBITS,
 parity=serial.PARITY_NONE,
 stopbits = serial.STOPBITS_ONE
)
buff=""
while 1:
	read = ser.read();
	#print(read)
	if read:
		if read=="\r":
			l = len(buff)
			#print(l)
			#for x in (buff):
			print(buff);
			buff=""
			res = raw_input()
			for i in range (0,len(res)):
				ser.write(res[i])
		else:
			buff+=(read);
	#ser.write('a')
	#time.sleep(1)

