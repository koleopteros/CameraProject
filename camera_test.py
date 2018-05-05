from picamera import PiCamera
from time import sleep
import os

def iso_test(cam):
    if not os.path.exists(__file__[:__file__.rfind('/')+1]+'iso_shots/'):
        os.makedirs(__file__[:__file__.rfind('/')+1]+'iso_shots/')
    cam.start_preview()
    cam.annotate_text = 'Beginning iso Tests!'
    sleep(0.5)
    for iso in range(100,800,50):
        cam.iso = int(iso)
        cam.annotate_text = 'ISO - '+str(iso)
        sleep(1.5)
        cam.capture(__file__[:__file__.rfind('/')+1]+'iso_shots/iso'+str(iso)+'.jpg')
    cam.stop_preview()
    
def exposure_test(cam):
    resolutions = [cam.MAX_RESOLUTION, (1280,900), (800,600)]
    cam.start_preview()
    cam.annotate_text = 'Beginning Exposure Tests!'
    sleep(0.5)
    for res in resolutions:
        cam.resolution = res
        if not os.path.exists(__file__[:__file__.rfind('/')+1]+str(res[0])+'x'+str(res[1])+'/'):
            os.makedirs(__file__[:__file__.rfind('/')+1]+str(res[0])+'x'+str(res[1])+'/')
        for mode in cam.EXPOSURE_MODES:
            cam.exposure_mode = str(mode)
            try:
                cam.annotate_text = str(mode)
                sleep(2)
                cam.capture(__file__[:__file__.rfind('/')+1]+str(res[0])+'x'+str(res[1])+'/'+str(mode)+'.jpg')
            except:
                print('error occurred during '+str(mode)+res)
    cam.annotate_text = 'Exposure Modes Complete!'
    sleep(0.5)
    cam.stop_preview()

def imgfx_test(cam):
    resolutions = [cam.MAX_RESOLUTION, (1280,900), (800,600)]
    cam.start_preview()
    cam.annotate_text = 'Starting Image Effects!'
    sleep(0.5)
    if not os.path.exists(__file__[:__file__.rfind('/')+1]+'image_fx/'):
        os.makedirs(__file__[:__file__.rfind('/')+1]+'image_fx/')
        
    for ifx in cam.IMAGE_EFFECTS:
        cam.resolution = resolutions[1]
        cam.image_effect = ifx
        cam.exposure_mode = 'auto'
        cam.annotate_text = str(ifx)
        sleep(0.75)
        cam.capture(__file__[:__file__.rfind('/')+1]+'image_fx/'+str(ifx)+'.jpg')
    cam.annotate_text = 'Test Complete!'
    sleep(0.5)
    cam.stop_preview()
