from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.tracer(0)
player_1 = Paddle(1)
player_2 = Paddle(2)

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.listen()
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()





screen.exitonclick()