from turtle import Turtle
alignment = "center"
font = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('purple')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align=alignment, font=font)

    def game_over(self):
        self.color('Red')
        self.goto(0,0)
        self.write(f'GAME OVER!', align=alignment, font=font)

    def score_rate(self):
        self.score += 1
        self.clear()
        self.update_score()