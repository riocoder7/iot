# --> gpss.py
# --> terminal  sudo python gpss.py

import serial 
import time 
import string
import pynmea2

while True:
    port = "/dev/ttyamao"
    ser = serial.Serial(port,baudrate=9600, timeout=0.5)
    dataout =  pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    if newdata[0:6] == "$GPRMC":
        newmsg=pynmea2.parse(newdata)
        lat=newmsg.latitude
        lng=newmsg.longitude
        gps=“Latitude=" +str(lat) + “and Longitude=" +str(lng)
        print(gps)