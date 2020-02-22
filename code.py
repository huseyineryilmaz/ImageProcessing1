import numpy as np
from PIL import Image

img = Image.open('originalPic.jpg')

def getPixel(img ,x ,y):
	pix = img.load()
	pixValues = pix
	print("Get Pixel = " + str(pixValues[x,y]))

getPixel(img, 53, 2)


def setPixel(img, x, y, a, b, c): # (x,y) location of pixel, (a,b,c) new rgb values of pixel
	pix = img.load()
	pixValues = pix
	print("Original pixel value = " + str(pixValues[x,y]))
	pixValues[x,y] = (a,b,c)
	print("New pixel Value = " + str(pixValues[x,y]))
setPixel(img,53,2,5,6,7)



def copyImage(img):
	imgCopy=img.copy()
	imgCopy.save('copyImage.png')

copyImage(img)



def luminanceGrayScale(img): #according to luminance formula red = red*0.299, green = green*0.587, blue = blue*0.114
	px = img.load()
	for y in range(img.height):
        	for x in range(img.width):
        		current_color = px[x,y]
        		new_color = (int(round(current_color[0] * 0.299)), int(round(current_color[1] * 0.587)), int(round(current_color[2] * 0.114)))
        		px[x,y] = new_color
	img.save('luminanceGrayScale.png')

luminanceGrayScale(img)




def grayScale(img):
	img = img.convert('LA')
	img.save('normalGrayScale.png')

grayScale(img)





def shiftPixel(img, v):
	px = img.load()
	for y in range(img.height):
        	for x in range(img.width):
        		current_color = px[x,y]
        		new_color = (current_color[0] + int(v), current_color[1] + int(v), current_color[2] + int(v))
        		px[x,y] = new_color
	img.save('shiftedPixel.png')

shiftPixel(img, 100)





def shiftPixelSolution(img, v):
	px = img.load()
	for y in range(img.height):
        	for x in range(img.width):
        		current_color = px[x,y]
        		new_color = (current_color[0] + int(v), current_color[1] + int(v), current_color[2] + int(v))
        		if new_color[0] + new_color[1] + new_color[2] > 525:
        			new_color = current_color
        		if new_color[0] + new_color[1] + new_color[2] < 225:
        			new_color = current_color
        		px[x,y] = new_color
	img.save('shiftPixelSolution.png')

shiftPixelSolution(img, 500)








