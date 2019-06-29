import PIL
import random
from PIL import Image
from PIL import ImageColor
import math

img = Image.open(r'ricePaddy.jpg')
img = img.convert('LA')

width, height = img.size
imgNew = Image.new('LA', (width, height))

print('generating...')

for x in range(width):
    for y in range(height):
        point = img.getpixel( (x,y) )[0]
        randNum = random.randint(0, 260)
        if randNum >= point:
            imgNew.putpixel( (x,y), (0, 255))
            

imgNew.save('ricePaddyStippled3.png')
