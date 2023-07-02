import turtle as t

ALIGNMENT="center"
FONT=("Bahnschrift SemiBold SemiConden", 70, "normal")

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore=0
        self.rightScore=0
        self.update()
        
    def update(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.leftScore, align=ALIGNMENT, font=FONT)
        self.goto(x=100,y=200)
        self.write(self.rightScore, align=ALIGNMENT, font=FONT)
        