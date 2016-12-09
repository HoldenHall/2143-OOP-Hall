import imageEdit
from PIL import Image
# Imports image library stuff
from io import BytesIO
import urllib.request
import sys

url = input('Enter the Url address for the file you wish to edit ')
file= BytesIO(urllib.request.urlopen(url).read())
img = Image.open(file)
x=0
Ie = ImageEd(img)

#simple menu used to call which effect you want

choice = input("1. Glass filter, 2. v_flip, 3. h_flip, 4. posterize, 5. blur, 6. solarize, 7. warhol")
while x<1:
    if choice == 1:
        distance = input("distance: ")
        img_out = input("image output: ")
        Ie.glass_filter(img,distance,img_out)
    if choice == 2:
        img_out = input("image output: ")
        Ie.v_flip(img,img_out)
    if choice == 3:
        img_out = input("image output: ")
        Ie.h_flip(img,img_out)
    if choice == 4:
        img_out = input("image output: ")
        snap = input("snap value: ")
        Ie.posterize(img,snap,img_out)
    if choice == 5:
        img_out = input("image output: ")
        kernel = input("kernel: ")
        Ie.blur(img,kernel,img_out)
    if choice == 6:
        img_out = input("image output: ")
        intensity = input("intensity: ")
        Ie.solarize(img,intensity,img_out)
    if choice == 7:
        img_out = input("image output: ")
        intensity = input("intensity: ")
        Ie.warhol(img,intensity,img_out)
    con = input("'y' or 'n' to continue")
    if con == 'y':
        x-1
    if con == 'n':
        x+1
