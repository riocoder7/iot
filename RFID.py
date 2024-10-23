# Write Code:


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
rfid = SimpleMFRC522()
try:
   print("Hold tag near the module...")
   rfid.write("Prof. Gufran")
   print("Written")
finally:
   GPIO.cleanup()

# Read Code:

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
rfid = SimpleMFRC522()
while True:
  id, text = rfid.read()
  print(id)
  print(text)