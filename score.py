import turtle
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lpoint = 0
        self.rpoint = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lpoint, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rpoint, align="center", font=("Courier", 80, "normal"))

    def lpoint_update(self):
        self.lpoint+=1
        self.update_score()

    def rpoint_update(self):
        self.rpoint += 1
        self.update_score()