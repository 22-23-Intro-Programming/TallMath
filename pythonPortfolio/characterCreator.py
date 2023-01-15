from Button import *
from graphics import *




def FourEyes():
    FE1 = Circle(Point(80,200),15)
    FE2 = Circle(Point(320,200),15)
    FE3 = Circle(Point(120,200),15)
    FE4 = Circle(Point(280,200),15)
    
    FE1.draw(win)
    FE2.draw(win)
    FE3.draw(win)
    FE3.draw(win)


def characterCreatorMain():
    global win
    win = GraphWin("Character Creator",400,400)


    #####################  8 buttons
    B_BigNose = Button(win, Point(0,0),Point(100,50),"red","Big Nose")
    B_SmallNose = Button(win, Point(0,50),Point(100,100),"blue","Small Nose")
    B_SharpFace = Button(win, Point(100,0),Point(200,50),"white","Sharp Face")
    B_SquareFace = Button(win, Point(100,50),Point(200,100),"green","Square Face")

    B_TwoEyes = Button(win, Point(200,0),Point(300,50),"pink","Two Eyes")
    B_FourEyes = Button(win, Point(200,50),Point(300,100),"purple","Four Eyes")
    B_Mouth = Button(win, Point(300,0),Point(400,50),"gray","Mouth")
    B_Quit = Button(win, Point(300,50),Point(400,100),"yellow","Quit")
    #####################

    #####################   shapes
    BN = Polygon(Point(200,200),Point(150,300),Point(250,300))
    SN = Polygon(Point(200,200),Point(180,250),Point(220,250))
    SpF = Polygon(Point(20,110),Point(380,110),Point(380,350),Point(200,380),Point(20,350))
    SF = Rectangle(Point(10,110),Point(390,390))

    TE1 = Circle(Point(100,200),30)
    TE2 = Circle(Point(300,200),30)
    FE1 = Circle(Point(80,200),15)
    FE2 = Circle(Point(320,200),15)
    FE3 = Circle(Point(120,200),15)
    FE4 = Circle(Point(280,200),15)

    Mouth = Polygon(Point(200,340),Point(120,315),Point(200,330),Point(280,315))
    
    #####################   shapes


    while True:
        m = win.getMouse()
        if B_BigNose.isClicked(m):
            SN.undraw()
            BN.undraw()
            BN.draw(win)
            BN.setFill("red")
        if B_SmallNose.isClicked(m):
            BN.undraw()
            SN.undraw()
            SN.draw(win)
            SN.setFill("blue")
        if B_SharpFace.isClicked(m):
            SpF.undraw()
            SF.undraw()           
            SpF.draw(win)
            SpF.setFill("white")
            
        if B_SquareFace.isClicked(m):
            SpF.undraw()
            SF.undraw()
            SF.draw(win)
            SF.setFill("green")
        if B_TwoEyes.isClicked(m):
            FE1.undraw()
            FE2.undraw()
            FE3.undraw()
            FE4.undraw()
            
            TE1.undraw()
            TE2.undraw()
            
            TE1.draw(win)
            TE2.draw(win)

            TE1.setFill("pink")
            TE2.setFill("pink")
        if B_FourEyes.isClicked(m):
            TE1.undraw()
            TE2.undraw()
            
            FE1.undraw()
            FE2.undraw()
            FE3.undraw()
            FE4.undraw()
            
            FE1.draw(win)
            FE2.draw(win)
            FE3.draw(win)
            FE4.draw(win)

            FE1.setFill("purple")
            FE2.setFill("purple")
            FE3.setFill("purple")
            FE4.setFill("purple")
        if B_Mouth.isClicked(m):
            Mouth.undraw()
            Mouth.draw(win)
            Mouth.setFill("grey")
        if B_Quit.isClicked(m):
            win.close()
            break
            
