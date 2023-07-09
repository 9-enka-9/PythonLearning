import turtle as t

FONT = ("Courier", 16, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-285,270)
        
        self.level=1
        self.updateScoreboard()
    
    def updateScoreboard(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', move=False, align="left", font=FONT)
    
    def increaseLevel(self):
        self.level+=1
        self.updateScoreboard()
        
    def gameOver(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align='center', font=FONT)
        
        