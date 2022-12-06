from graphics import *
from Button import *

original_data = []
win = GraphWin("Image Editor",400,400)


def dkn(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0],pix[1],pix[2]
            newColor = color_rgb(int(float(r)*0.741),int(float(g)*0.741),int(float(b)*0.741))
            img.setPixel(i,j,newColor)
            
    return True

def ltn(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0],pix[1],pix[2]
            newColor = color_rgb(r+int(float(255-r)*0.3),g+int(float(255-g)*0.3),b+int(float(255-b)*0.3))
            img.setPixel(i,j,newColor)
            
    return True


def gS(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            newC = int((pix[0]+pix[1]+pix[2])/3)
            newColor = color_rgb(newC,newC,newC)
            img.setPixel(i,j,newColor)
            
    return True


def ctr(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0],pix[1],pix[2]
            
            Avg = int((pix[0]+pix[1]+pix[2])/3)
            if Avg >= 128:   
                newColor = color_rgb(r+int(float(255-r)*0.3),g+int(float(255-g)*0.3),b+int(float(255-b)*0.3))
                img.setPixel(i,j,newColor)
            else:
                newColor = color_rgb(int(float(r)*0.741),int(float(g)*0.741),int(float(b)*0.741))
                img.setPixel(i,j,newColor)        
    return True

def rd(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0],pix[1],pix[2]
            GrayScaleColor = int((pix[0]+pix[1]+pix[2])/3)
            
            newColor = color_rgb(r,GrayScaleColor,GrayScaleColor)
            img.setPixel(i,j,newColor)
            
    return True


def bl(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0],pix[1],pix[2]
            GrayScaleColor = int((pix[0]+pix[1]+pix[2])/3)
            
            newColor = color_rgb(GrayScaleColor,b,GrayScaleColor)
            img.setPixel(i,j,newColor)
            
    return True

def save_original_data(img):
    x = img.getWidth()
    y = img.getHeight()

    n = 0
    
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r,g,b = pix[0],pix[1],pix[2]
            original_data.append([r,g,b])
            n = n+1
            
            
    return True

def rst(img):
    x = img.getWidth()
    y = img.getHeight()

    n = 0
    
    for i in range(x):
        for j in range(y):
            pix  = original_data[n]
            r,g,b = pix[0],pix[1],pix[2]
            img.setPixel(i,j,color_rgb(r,g,b))
            n = n+1
            
            
    return True



def main():
    
    I = Image(Point(200,250),"eee.png")
    I.draw(win)
    
    save_original_data(I)#save data for "reset" method

    
    lighten = Button(win, Point(0,0),Point(100,50),"pink","Lighten")
    darken = Button(win, Point(0,50),Point(100,100),"purple","Darken")
    grayScale = Button(win, Point(100,0),Point(200,50),"white","Gray Scale")
    contrast = Button(win, Point(100,50),Point(200,100),"green","Contrast")

    red = Button(win, Point(200,0),Point(300,50),"red","Red")
    blue = Button(win, Point(200,50),Point(300,100),"blue","Blue")
    reset = Button(win, Point(300,0),Point(400,50),"gray","Reset")

    Quit = Button(win, Point(300,50),Point(400,100),"yellow","Quit")

    while True:
        m = win.getMouse()
        if lighten.isClicked(m):
            ltn(I)
        if darken.isClicked(m):
            dkn(I)
        if grayScale.isClicked(m):
            gS(I)
        if contrast.isClicked(m):
            ctr(I)
        if red.isClicked(m):
            rd(I)
        if blue.isClicked(m):
            bl(I)
        if reset.isClicked(m):
            rst(I)
        if Quit.isClicked(m):
            win.close()
            break
            


if __name__ == "__main__":
    main()
