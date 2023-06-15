from turtle import Turtle,Screen

t=Turtle()
scr=Screen()

def forward():
    t.fd(10)
    
def backward():
    t.bk(10)

def counterclockwise():
    t.left(10)
    
def clockwise():
    t.right(10)

def clearScreen():
    t.home()
    t.clear()
    
scr.listen()

scr.onkeypress(key="w",fun=forward)
scr.onkeypress(key="s", fun=backward)
scr.onkeypress(key="a", fun=counterclockwise)
scr.onkeypress(key="d",fun=clockwise)
scr.onkeypress(key="c", fun=clearScreen)

scr.exitonclick()
    
