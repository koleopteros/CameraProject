import os

from PIL import Image as img


im = img.open('test3.png')
print(im.format,im.size,im.mode)

for root,dirs,files in os.walk(".\800x600"):
    print(root)
    #for d in dirs:
    #    print(dirs)
    for filename in files:
        print(filename)
im.show()
