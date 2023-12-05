FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.score = 0
        self.goto(240, 240)
        self.write("LEVEL: "+str(self.level), align="right", font=FONT)
        self.goto(-240, 240)
        self.write("SCORE: "+str(self.score), align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_incr(self):
        self.clear()
        self.level += 1
        self.score += 5
        self.goto(-240, 240)

        self.write("SCORE: "+str(self.score), align="left", font=FONT)
        self.goto(240, 240)

        self.write("LEVEL: "+str(self.level), align="right", font=FONT)

