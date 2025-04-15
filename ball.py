import turtle
from turtle import Turtle

BALL_POSITION=(0,0)
INI_SPEED=200
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_self()
        self.x_move=10
        self.y_move = 10


    def create_self(self):
        self.shape("circle")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(BALL_POSITION)
        
    def move_ball(self):
        self.speed(INI_SPEED)
        new_x=self.xcor()+self.x_move
        new_y=self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def collide_y(self):
        self.y_move *= -1
        self.speed(INI_SPEED+10)
    def collide_x(self):
        self.x_move *= -1
        self.speed(INI_SPEED + 10)

    def repos(self):
        self.goto(0,0)
        self.collide_x()



