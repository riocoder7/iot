import RPi.GPIO as GPIO
import time;
GPIO.setwarnings(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
while 1:
    time.sleep(.4)
    print("led on ")
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)

    time.sleep(.4)
    print("led on ")
    GPIO.output(17,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)

    time.sleep(.4)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)

    time.sleep(.4)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.HIGH)



