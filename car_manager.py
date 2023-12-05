COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.left(180)
        self.penup()
        self.goto(random.randint(350, 550), random.randint(-210, 400))
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))

    def car_move(self):
        self.forward(10)



