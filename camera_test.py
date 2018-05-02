from picamera import PiCamera
from time import sleep
import os

'''
This script tests the camera's exposure modes and saves a sample image of 
that mode in different resolutions defined in the 'resolutions' tuple
'''

cam = PiCamera()
#change rotation based off hardware camera positioning.
#rotation 0 if hardware ribbon is at the bottom of the camera module
cam.rotation = 180
cam.framerate = 25
cam.awb_mode = 'auto'

resolutions = (cam.MAX_RESOLUTION,(1280,900),(800,600))

#get camera rolling...
cam.start_preview()
for res in resolutions:
	cam.resolution = res
	(os.makedirs(__file__[:__file__.rfind('/')+1]+str(res[0])+'x'+str(res[1])+'/'),None) \
	[os.path.exists(__file__[:__file__.rfind('/')+1]+str(res[0])+'x'+str(res[1])+'/')]
	for mode in cam.EXPOSURE_MODES:
		cam.exposure_mode = str(mode)
		#begin attempt to capture image with an annotation describing mode
		try:
			cam.annotate_text = str(mode)
			#give camera CMOS sensor time to adjust image to proper exposure
			sleep(2)
			cam.capture(__file__[:__file__.rfind('/')+1]+str(res[0])+'x'+str(res[1])+'/'+str(mode)+'.jpg')
		except:
			print('error occured during capture of '+str(mode)+' '+res)
cam.annotate_text = 'Test has concluded...'
sleep(2)
cam.annotate_text = 'Good Bye!'
sleep(1)
cam.stop_preview()
cam.close()	