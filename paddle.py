from turtle import Turtle

WIDTH = 20
HEIGHT = 100
LEFT_X_POSITION = -350
RIGHT_X_POSITION = 350
CENTER_Y_POSITION = 0


class Paddle(Turtle):

    def __init__(self, player_number):

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
        if player_number == 1:
            self.goto(LEFT_X_POSITION, CENTER_Y_POSITION)
        elif player_number == 2:
            self.goto(RIGHT_X_POSITION, CENTER_Y_POSITION)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
