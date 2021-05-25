from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
camera.rotation = 180 #rotating angle 5 degrees.

'''preview on raspberry pi connected screen. This doesn't work through VNC/SSH'''
camera.start_preview() #at least 2nds to camera's light sensor to be ready
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
sleep(5)
camera.capture('/home/pi/Desktop/image2.jpg')
camera.stop_preview()

'''testing recording'''
# camera.start_preview()
# sleep(5)
# camera.start_recording('/home/pi/Desktop/video.h264')
# sleep(10)
# camera.stop_recording('/home/pi/Desktop/video.h264')
# camera.stop_preview()