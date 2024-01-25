from turtle import Turtle

STRETCH_WID = 5
STRETCH_LEN = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_up_l(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down_l(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        