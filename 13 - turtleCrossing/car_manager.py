import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self) -> None:
        self.allCars=[]
        self.carSpeed=STARTING_MOVE_DISTANCE
    
    def createCar(self):
        randChance=random.randint(1,10)
        if randChance!=1:
            return
        newCar = t.Turtle(shape="square")
        newCar.shapesize(stretch_len=2,stretch_wid=1)
        newCar.penup()
        newCar.color(random.choice(COLORS))
        randY=random.randint(-250,220)
        newCar.goto(300,randY)
        self.allCars.append(newCar)
        
    def moveCar(self):
        if len(self.allCars) <= 25:
            for car in self.allCars:
                car.backward(self.carSpeed)
        else:
            for i in range(len(self.allCars)-25,len(self.allCars),1):
                self.allCars[i].backward(STARTING_MOVE_DISTANCE)
    
    def levelUp(self):
        self.carSpeed+=MOVE_INCREMENT
        
            
        
        
