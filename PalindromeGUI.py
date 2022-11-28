from graphics import *
from Button import *

def isPalindrome(text):
    s = len(text)
    txet  = ""
    for i in range(s):
        txet += text[s-i-1]

    if txet == text:
        return True
    else:
        return False
        




def main():
    win = GraphWin("Palindrome",800,600)
    win.setBackground("beige")

    Q = Button(win,Point(650,500),Point(750,575),"tomato","QUIT")
    P = Button(win,Point(350,350),Point(450,425),"cyan","Check!")
    


    E = Entry(Point(400,300),30)
    E.setFill("white")
    E.draw(win)

    T = Text(Point(400,250),"Write Something That You Think Is a Palindrome.")
    T.draw(win)

    Ts = Text(Point(400,480),"The input is a palindrome! :)")
    Tf = Text(Point(400,480),"The input is NOT a palindrome :(")
    
    
    while True:
        m = win.getMouse()
        
        if Q.isClicked(m):
            break
        if P.isClicked(m):
            if isPalindrome(E.getText()):
                Ts.undraw()
                Tf.undraw()
                Ts.draw(win)
            else:
                Ts.undraw()
                Tf.undraw()
                Tf.draw(win)
                

        
    win.close()


if __name__ == "__main__":
    main()
