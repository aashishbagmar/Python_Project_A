from turtle import Turtle
FONT = ("Arial", 22, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.updatescore()
