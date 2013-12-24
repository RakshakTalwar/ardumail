ardumail
========

Python script that interacts with an Arduino to notify you when you have a new email.

To use: 

1. Hook up an LED to pin 13 on your Arduino (or use the onboard led). 
2. Connect your Arduino to your computer with a USB cable. 
3. Start up the Arduino IDE and upload the ardumail.ino file to the Arduino.
4. Open the ardumail.py file with a text editor.
5. Edit the python script with the serial port your Arduino is connected to (found on bottom left of Arduino IDE), your
email address, and your password. 
6. Save and run the ardumail.py script. The LED should now turn on when you have an unread email.
