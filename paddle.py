from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):

    def __init__(self, position):

        # Create a turtle object from superclass.
        super().__init__()
        self.penup()

        # Set heading facing north since movement is forwards (up) and backwards (down).
        self.setheading(90)

        # Set shape, color and set size of paddle.
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=(int(HEIGHT/20)), stretch_wid=(int(WIDTH/20)))

        # Set position of paddle given input argument.
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
