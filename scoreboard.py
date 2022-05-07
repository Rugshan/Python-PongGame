from turtle import Turtle

FONT = ("Courier", 48, "bold")

class Scoreboard(Turtle):

    def __init__(self):

        # Create turtle.
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        # Score Attributes
        self.left_score = 0
        self.right_score = 0

        # Write Scoreboard
        self.update_scoreboard()

    def increment_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increment_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=FONT)
