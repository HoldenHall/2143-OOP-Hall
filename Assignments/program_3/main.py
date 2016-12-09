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
Ie = ImageEd()
choice = input("1. Glass filter, 2. v_flip, 3. h_flip, 4. posterize, 5. blur, 6. solarize, 7. warhol")
while x<1:
    if choice == 1:
        Ie.glass_filter
    if choice == 2:
        Ie.v_flip
    if choice == 3:
        Ie.h_flip
    if choice == 4:
        Ie.posterize
    if choice == 5:
        Ie.blur
    if choice == 6:
        Ie.solarize
    if choice == 7:
        Ie.warhol
    con = input("'y' or 'n' to continue")
    if con == 'y':
        x-1
