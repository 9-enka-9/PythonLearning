import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goToStart()
        self.setheading(to_angle=90)
    
    def goUp(self):
        self.forward(MOVE_DISTANCE)
        
    def goToStart(self):
        self.goto(STARTING_POSITION)
        
    def isAtFinishLine(self):
        if self.ycor()>280:
            return True
        return False
        
    
