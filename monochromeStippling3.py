import PIL
import random
from PIL import Image
from PIL import ImageColor
import math

img = Image.open(r'C:\Users\Marius Ygonia\pythonScripts\ricePaddy.jpg')
img = img.convert('LA')

def roundDown(x):
    return int(math.floor(x / 10.0)) * 10

def dotIt():
    imgNew.putpixel( (x,y), (0, 255))

width, height = img.size
imgNew = Image.new('LA', (width, height))

print('generating...')

for x in range(width):
    for y in range(height):
        point = img.getpixel( (x,y) )[0]
        randNum = random.randint(0, 260)
        if randNum >= point:
            dotIt()
            

imgNew.save('ricePaddyStippled3.png')
