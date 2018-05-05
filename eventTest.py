from picamera import PiCamera
from time import sleep
import os


cam = PiCamera()
cam.rotation = 180
cam.framerate = 30
cam.awb_mode = 'auto'
resolutions = [cam.MAX_RESOLUTION, (1280,900), (800,600)]

counter = 0
cam.resolution = resolutions[0]

cam.start_preview()

while True:
    isDone = input('Enter x to exit')
    if isDone=='x':
        break
    for i in range(3):
        cam.annotate_text=str(3-i)
        sleep(0.75)
    cam.annotate_text='Smile!'
    sleep(0.25)
    cam.annotate_text=''
    cam.capture(__file__[:__file__.rfind('/')+1]+'image_'+str(counter)+'.jpg')
    counter = counter+1
cam.stop_preview()
cam.close()
