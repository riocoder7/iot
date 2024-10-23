import picamera
import PiCemera
import time

camera = PiCemera()
camera.resolution=(1280,780)

camera.start_preview()
camera.start_recording('home/pi/desktop/cemera/video.h264')

for i in range(5):
    time.sleep(5)
    camera.capture('/home/pi/Desktop/cemera/images%s.jpg'%i)


camera.stop_recording()
camera.stop_preview()
    