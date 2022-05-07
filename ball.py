from turtle import Turtle

MOVE_AMOUNT = 3
DEFAULT_HEADING = 65

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(DEFAULT_HEADING)
        self.move_amount = MOVE_AMOUNT

    def move(self):
        self.forward(self.move_amount)

    def detect_wall_collision(self):

        # Check if ball has hit upper wall.
        if self.ycor() > 280:

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
        elif self.ycor() < -280:

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

    def detect_paddle_collision(self, player_1, player_2):

        # Check collision with left (player 1) paddle.
        if self.distance(player_1) < 50 and self.xcor() < -320:

            if 90 <= self.heading() <= 180:
                angle_of_reflection = 180 - 90 - (180 - self.heading())
                new_heading = angle_of_reflection
                self.setheading(new_heading)

            elif 180 <= self.heading() <= 270:
                angle_of_reflection = 180 - 90 - (self.heading() % 90)
                new_heading = 360 - angle_of_reflection
                self.setheading(new_heading)

            return True

        # Check collision with right (player 2) paddle.
        elif self.distance(player_2) < 50 and self.xcor() > 320:

            if 0 <= self.heading() <= 90:
                angle_of_reflection = 180 - 90 - self.heading()
                new_heading = 180 - angle_of_reflection
                self.setheading(new_heading)

            elif 270 <= self.heading() <= 360:
                angle_of_reflection = 180 - 90 - (360 - self.heading())
                new_heading = 180 + angle_of_reflection
                self.setheading(new_heading)

            return True

        return False

    def reset_position(self):
        self.goto(0, 0)
        self.setheading((self.heading() + 180) % 360)

    def detect_paddle_miss(self):

        if self.xcor() > 380:
            self.reset_position()
            return "RIGHT"

        elif self.xcor() < -380:
            self.reset_position()
            return "LEFT"

    def increase_speed(self):
        self.move_amount += 0.3

    def reset_speed(self):
        self.move_amount = MOVE_AMOUNT

