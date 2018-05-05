from PIL import Image as img

img_1 = img.open('test1.png')
img_2 = img.open('test2.png')

img.alpha_composite(img_2,img_1).save('test3.png')
