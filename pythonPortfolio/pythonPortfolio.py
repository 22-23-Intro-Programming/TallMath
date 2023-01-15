from Button import *
from PBset1 import *
from PBset2 import *
from PBset3 import *
from imageEditor import *
from characterCreator import *
from graphics import *

def main():
    win = GraphWin("Python Portfolio",600,600)


    IE = Button(win, Point(0,0),Point(200,100),"yellow","Image Editor")
    T_IE = Text(Point(400,50),"This is a image editor that is able to perform 'lighten,' 'darken' \n and other functions of a picture")
    T_IE.draw(win)

    

    PB1 = Button(win, Point(0,100),Point(200,200),"pink","Problem Set 1")
    T_PB1 = Text(Point(400,150),"This is a set of functions including 'Greeting,'  a multiple testor, \n and a palindrome testor")
    T_PB1.draw(win)

    PB2 = Button(win, Point(0,200),Point(200,300),"red","Problem Set 2")
    T_PB2 = Text(Point(400,250),"This is a set of functions including a factorial Calculator, a string doubler \n and a camelcase convertor")
    T_PB2.draw(win)

    PB3 = Button(win, Point(0,300),Point(200,400),"green","Problem Set 3")
    T_PB3 = Text(Point(400,350),"This is a set of functions including a currency convertor and \n a grocery list calculator")
    T_PB3.draw(win)
    
    CC = Button(win, Point(0,400),Point(200,500),"yellow","Character Creator")
    T_CC = Text(Point(400,450),"This is a character creator that helps you make a random monster :)")
    T_CC.draw(win)

    
    Quit = Button(win, Point(0,500),Point(200,600),"tomato","Quit")
    
    while True:
        m = win.getMouse()
            
        if IE.isClicked(m):
            imageEditorMain()
        if PB1.isClicked(m):
            PB1main()
        if PB2.isClicked(m):
            PB2main()
        if PB3.isClicked(m):
            PB3main()
        if CC.isClicked(m):
            characterCreatorMain()

        if Quit.isClicked(m):
            win.close()
        
        


if __name__ == "__main__":
    main()
