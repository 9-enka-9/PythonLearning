import turtle as t
ALIGNMENT= "center"
FONT = ('JetBrains Mono Bold', 16, 'normal')

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('11 - SnakeGame\\data.txt',mode='r') as file:
            self.content=file.read()
            file.close()
        self.highScore=int(self.content)
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.updateScore()
    
    def updateScore(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}  |  High Score: {self.highScore}",move=False, align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.highScore:
            self.highScore=self.score
            with open('11 - SnakeGame\\data.txt',mode='w') as file:
                file.write(f'{self.highScore}')
                file.close()
        self.score=0
        self.updateScore()
        
    # def gameOver(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
       
        