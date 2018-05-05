from picamera import PiCamera
from time import sleep
import camTest
import os
import sys


cam = PiCamera()
cam.rotation = 180
cam.framerate = 30
cam.awb_mode = 'auto'
cam.sharpness = 30

try:
    camTest.imgfx_test(cam)
except:
    print('unexpected error...')
    (None, cam.stop_previewing())[cam.previewing()]
    cam.close()
    
cam.annotate_text = 'Shutting Down'
sleep(1)
cam.close()
print('Done!')
