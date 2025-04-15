#importing modules
import turtle
from paddle import Paddles
from turtle import Screen
from time import sleep
from ball import Ball
from score import Score
#creating screen objects
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Bhoomika's pong game")
screen.tracer(0)

#creating objects
r_paddle=Paddles((350,0))
l_paddle=Paddles((-350,0))
ball=Ball()
score=Score()

screen.listen()
#Moving right paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

#Moving left paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on=True
while game_is_on:

    sleep(0.15)
    ball.move_ball()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.collide_y()


    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collide_x()

    if ball.xcor()>380 :
        score.lpoint_update()
        print(f"Game over for right ")
        ball.repos()

    elif ball.xcor() < -380:
        score.rpoint_update()
        print(f"Game over for left")
        ball.repos()
        #increase the score of opossite person
        #start the game in opposte persons bound

    screen.update()


screen.exitonclick()