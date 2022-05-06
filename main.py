from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

import time

PLAYER_1_POSITION = (-350, 0)
PLAYER_2_POSITION = (350, 0)
SLEEP = 0.01

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

player_1 = Paddle(PLAYER_1_POSITION)
player_2 = Paddle(PLAYER_2_POSITION)
ball = Ball()


screen.listen()
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(SLEEP)
    screen.update()
    ball.move()
    ball.detect_wall_collision()





screen.exitonclick()