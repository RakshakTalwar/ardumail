"""This Python script will check a gmail account for unread emails. If an unread email is detected the script uses the serial library to output a '1' to the serial port which is picked up by an Arduino. The Arduino then turns on an LED to notify the user that they have an unread email.

Open Source under The MIT License

Written by Rakshak Talwar on 12/23/2013
"""

import imaplib, serial #import modules

ser = serial.Serial('your_serial_port_here', 9600) #create serial object, enter in the proper port 
obj = imaplib.IMAP4_SSL('imap.gmail.com') #create imap object, set to gmail
obj.login('your_email@gmail.com', 'PASSW0RD') #enter in gmail credentials

#runs continuously 
while 1: 
	obj.select() #refresh 
	val = len(obj.search(None, 'UnSeen')[1][0].split()) #generate a value of 1 or 0
        #print "The val is: %s\n" %  val #print value to monitor
        ser.write(str(val)) #write value to serial port
