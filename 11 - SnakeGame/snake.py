import turtle as t

MOVE_DISTANCE=20
RIGHT=0
UP=90
LEFT=180
DOWN=270

class Snake():
    snake=[]
    segNum=0
    def __init__(self):
        for i in range(3):
            self.createSegment()
            self.segNum+=1
    
    def createSegment(self):
        newSquare=t.Turtle(shape="square")
        newSquare.color("white")
        newSquare.pensize(width=20)
        newSquare.penup()
        newSquare.speed(120)
        if len(self.snake)==0:
            newSquare.goto(0,0)
        else:
            newSquare.goto(self.snake[self.segNum-1].xcor()-20, self.snake[self.segNum-1].ycor())
        self.snake.append(newSquare)
    
    def move(self):
        for segNumb in range(len(self.snake)-1, 0, -1):
            self.snake[segNumb].goto(self.snake[segNumb-1].pos())
        self.snake[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.snake[0].heading()==DOWN:
            return
        self.snake[0].setheading(90)
    
    def down(self):
        if self.snake[0].heading()==UP:
            return
        self.snake[0].setheading(270)
    
    def left(self):
        if self.snake[0].heading()==RIGHT:
            return
        self.snake[0].setheading(180)
        
    def right(self):
        if self.snake[0].heading()==LEFT:
            return 
        self.snake[0].setheading(0)
        