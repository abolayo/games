from turtle import Turtle

FONT = ('Ariel', 20, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score} , High Score: {self.high_score}', True, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 2
        self.write_score()

    def foul(self):
        self.score -= 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            with open("score.txt", mode="w") as value:
                value.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update()

    def reset_game(self):
        response = input("Do you want to reset the game? (y/n) :")
        if response == "y":
            with open("score.txt", mode="w") as value:
                value.write(str(0))
            print("Game Reset")
