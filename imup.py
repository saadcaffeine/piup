#!/usr/bin/env python
import socket
import sys
import imp
caffk = imp.load_compiled("caffk", "/home/pi/py_modules/caffk.pyc")
# attempts to connect to an external host, to help identify itself and announce its own addres
# uses ip to avoid DNS issues

# announcing via PushBullet
from pushbullet import Pushbullet
pb = Pushbullet(caffk.api_key)

friendlyHost = "113.197.38.104"
myip = ""#qua?
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	s.connect((friendlyHost,80))
	myip = s.getsockname()[0]
	print(myip)
except socket.error, (value,message): 
    	if s: 
        	s.close() # lets be polite.
		print "Closed."
    	print "Could not open socket: " + message 
    	sys.exit(1) 

push = pb.push_note("pipi2 " + myip,"I can reach: " +  friendlyHost)
if s:
	s.close()
	print "Done."
sys.exit(1)
#s.close()

