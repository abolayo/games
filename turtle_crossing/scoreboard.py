from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color('Black')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write_score()

    def write_score(self):
        self.write(f'Level: {self.score} ', False, align="left", font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)



