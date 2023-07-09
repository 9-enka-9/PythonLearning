import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
carManager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.goUp,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    
    carManager.createCar()
    carManager.moveCar()
    
    # Detect collision with car
    for car in carManager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()
            break
    
    #Detect successful crossing
    if player.isAtFinishLine():
        player.goToStart()
        carManager.levelUp()
        scoreboard.increaseLevel()






screen.exitonclick()