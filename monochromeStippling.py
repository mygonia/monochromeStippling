import PIL
import random
from PIL import Image
from PIL import ImageColor


img = Image.open(r'C:\Users\Marius Ygonia\pythonScripts\grayscaleBar.jpg')
img = img.convert('LA')

width, height = img.size
print('stippling...')

img.save('Monochrome.png')
imgNew = Image.new('LA', (width, height))

for x in range(width):
    for y in range(height):
        point = img.getpixel((x, y))
        darkness = point[0]
        randNum = random.randint(0, 100)
        if darkness <= 37:
            if randNum >= 5:
                imgNew.putpixel( (x,y),(0, 255))
            continue
        if darkness > 37 and darkness <= 74:
            if randNum >= 20:
                imgNew.putpixel( (x,y), (0, 255))
            continue
        if darkness > 74 and darkness <= 111:
            if randNum >= 30:
                imgNew.putpixel( (x,y), (0, 255))
            continue
        if darkness > 111 and darkness <= 148:
            if randNum >= 40:
                imgNew.putpixel( (x,y), (0, 255))
            continue
        if darkness > 148 and darkness <= 185:
            if randNum >= 50:
                imgNew.putpixel( (x,y), (0, 255))
            continue
        if darkness > 185 and darkness <= 222:
            if randNum >= 60:
                imgNew.putpixel( (x,y), (0, 255))
            continue
        if darkness > 222:
            if randNum >= 90:
                imgNew.putpixel( (x,y), (0, 255))
            continue

imgNew.save('grayscaleBar.png')
