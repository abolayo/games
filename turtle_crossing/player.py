from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.goto_start()
        self.left(90)

    def move_forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def goto_start(self):
        self.goto(STARTING_POSITION)
