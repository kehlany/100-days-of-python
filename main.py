from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
ball = Ball()

scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(height = 600, width= 800)
screen.title("Pong")
l_paddle = Paddle((350,0))
r_paddle = Paddle((-350, 0))


screen.listen()

screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
screen.tracer(0)
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() > 380:
        ball.deflect_y()
    if ball.distance(r_paddle)< 50 and ball.xcor() >320 or ball.distance(l_paddle)< 50 and ball.xcor() >320:
        ball.deflect_x()
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -280:
        ball.refresh()
        scoreboard.r_point()





screen.exitonclick()
