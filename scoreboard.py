from turtle import Turtle
from snake import Snake

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            content = file.read()
            print(content)
            if content:
                self.high_score = int(content)
            else:
                self.high_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f'Score:  {self.score}  High Score:  {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()
