from turtle import Turtle

MOVE_AMOUNT = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(32)

    def move(self):
        self.forward(MOVE_AMOUNT)
