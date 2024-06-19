from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # it will crete a scoreboard on the top
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score_update()

    def score_update(self):
        self.write(f"score {self.score}", align="center", font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 18, 'normal'))

    def update_score(self):  # it will update the score on the display
        self.score += 1
        self.clear()
        self.score_update()
