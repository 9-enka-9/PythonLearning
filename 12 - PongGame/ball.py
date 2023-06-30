import turtle as t
from random import randint

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("white")
        self.penup()
        self.xMove=1
        self.yMove=1
    
    def move(self):
        x=self.xcor()+self.xMove
        y=self.ycor()+self.yMove
        self.goto(x=x,y=y)
        
    def bounce(self):
        self.yMove*=-1