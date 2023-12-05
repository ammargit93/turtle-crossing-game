import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

carList = []

scoreboard = Scoreboard()
player = Player()
screen.onkeypress(fun=player.move_turtle, key="Up")

counter = 0
i = 0.1

game_is_on = True
while game_is_on:
    time.sleep(i)
    screen.update()

    counter += 1

    if counter % 3 == 0:
        car = CarManager()
        carList.append(car)

    for car in carList:
        car.car_move()
        if car.xcor() < -320:
            carList.remove(car)

    for car in carList:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.ycor() > 280:
            scoreboard.level_incr()
            i *= 0.7
            player.goto(0,-280)


screen.exitonclick()