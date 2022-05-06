from turtle import Turtle

MOVE_AMOUNT = 2
DEFAULT_HEADING = 85

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(DEFAULT_HEADING)

    def move(self):
        self.forward(MOVE_AMOUNT)

    def detect_wall_collision(self):

        # Check if ball has hit upper wall.
        if self.ycor() > 300:

            # Check if ball is travelling right (upwards).
            if 0 <= self.heading() <= 90:
                angle_of_reflection = 180 - 90 - self.heading()
                new_heading = 270 + angle_of_reflection
                self.setheading(new_heading)

            # Check if ball is travelling left (upwards).
            elif 90 <= self.heading() <= 180:
                angle_of_reflection = 180 - 90 - (180 - self.heading())
                new_heading = 270 - angle_of_reflection
                self.setheading(new_heading)

        # Check if ball has hit lower wall.
        elif self.ycor() < -300:

            # Check if ball is travelling left (downwards).
            if 180 <= self.heading() <= 270:
                angle_of_reflection = 180 - 90 - (self.heading() % 90)
                new_heading = 90 + angle_of_reflection
                self.setheading(new_heading)

            # Check if ball is travelling right (downwards).
            elif 270 <= self.heading() <= 360:
                angle_of_reflection = 180 - 90 - (360 - self.heading())
                new_heading = 90 - angle_of_reflection
                self.setheading(new_heading)
