from PIL import Image, ImageDraw
import random
import sys


def recolor(x1, y1, x2, y2):
    pixR = random.randint(-20, 20)
    pixG = random.randint(-20, 20)
    pixB = random.randint(-20, 20)
    pixRR = random.randint(-0,   150)
    pixGG = random.randint(-150, 150)
    pixBB = random.randint(-150, 150)    
    
    """
    pixR = -40
    pixG = 30
    pixB = 30
    """
    #print pixR, pixG, pixB
    if random.randint(0, 20) >= 4 :
        #print (pixR, pixG, pixB)
        for x in range(x1, x2) :
            for y in range (y1, y2) :            
                pix[x, y] = (pix[x,y][0]+pixR, pix[x,y][1]+pixG, pix[x,y][2]+pixB)
    else : 
        #print (pixRR, pixGG, pixBB)
        for x in range(x1, x2) :
            for y in range (y1, y2) :            
                pix[x, y] = (pixRR, pixGG, pixBB)        

def warp (x1, y1, x2, y2, amount) :
    for x in range(x1, x2) :
        for y in range (y1, y2) :
            if x+amount < im.size[0] :
                pix[x, y] = pix[x+amount, y]

def cut (xAmount, yAmount):
    yAmount = yAmount
    fullX = int(im.size[0] // xAmount)
    fullY = int(im.size[1] // yAmount)
    for y in range (0, int(yAmount)) :
        for x in range (0, int(xAmount)) :
            if random.randint(0, 20) >= 12 : #warp
                warp (fullX*x, fullY*y, fullX*x + fullX, fullY*y + fullY, random.randint(1,10)*3)
            if random.randint(0, 10) >= 2 : #recolor
                recolor (fullX*x, fullY*y, fullX*x + fullX, fullY*y + fullY)

def main (argv) :
    global im
    im = Image.open('image1.jpg')
    global pix
    pix = im.load()
    dr = ImageDraw.Draw(im)
    cutx = int(im.size[0] / 120)
    cuty = int(im.size[1] / 8)
    print (cutx, cuty, "cutx, cuty")
    cut(cutx, cuty)
    #recolor(0, 0, im.size[0], im.size[1]) 
    im.save('image2.jpg')
    im.show('image2.jpg')
    del dr    

main(sys.argv[1:])