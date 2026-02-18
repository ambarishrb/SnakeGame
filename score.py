from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.write(f"Score = {self.score}",move=False,align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER",align="center",font=("Arial",24,"bold"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}",move=False,align="center",font=("Arial",24,"normal"))