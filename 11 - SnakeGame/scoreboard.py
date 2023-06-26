import turtle as t
ALIGNMENT= "center"
FONT = ('Yeseva One', 20, 'normal')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.write(arg=f"Score: {self.score}",move=False, align=ALIGNMENT, font=FONT)
    
    def updateScore(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}",move=False, align=ALIGNMENT, font=FONT)
        
    def gameOver(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        
        