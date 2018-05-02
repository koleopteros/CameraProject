# CameraProject
## Introduction
This project is to build a camera app using python.

This will be updated as the project progresses.

## Programming To do List
 - complete GPIO button control test
 - create image overlay functions
 - complete image overlay test on existing image files
 - implement image overlay on camera preview
 - Build GUI interface that will control the camera
 - Do live testing

## Build/Buy/Review List
 - Review available Raspberry Pi cameras

## Issues
Currently, dealing with some issues, Rolling shutter, colour imbalance(IR interference?), and a case or frame to keep the whole setup stable.

### On the Rolling Shutter:
Images are coming in kind of split into 2-3 sections of differing brightness

Perhaps something is wrong with the circuit of my old flashlight, thus causing it to 'flicker' at a strange frequency?  I don't know.

Current solution: buy a new LED light source.

### On colour imbalance:
I suspect it is due to IR interference as my camera does not have a built in IR filter.

Potential solution: Get some sort of IR or heat filter film to overlay on the camera itself

Last ditch solution: Buy a Raspberry Pi camera with a built in IR filter.

### Device Case/Frame stability:
Current issue with this is that the device has a free hanging camera, not cool. Also, the RPI seems to be heating up rather quickly, reaching 80~ degrees fahrenheit.  Not good if I plan to run it for long periods in a crowded environment.

Planned solution: build a cheap case and frame to hold up the device at an appropriate height.  Perhaps 3-D print a case?

Last ditch solultion: Buy all the things... blow $30 on a case, maybe another 30 bucks on lumber to build a frame.