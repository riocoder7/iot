import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
display = tm1637.TM1637(11,8,tm1637.BRIGHT_TYPICAL)
display.clear()
display.setBrightnes(1)

while(True):
    now = datetime.datetime.now()
    hour = now.hour
    min = now.minute
    secound  = now.second
    current_time = [int(hour/10),hour%10,int(min/10),min%10]
    display.Show(current_time)
    display.ShowDoublepoint(secound%2)
    time.sleep(1)
    