from turtle import Turtle
from utilities import get_players, draw_line


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.color("red")
        self.p1, self.p2 = get_players()
        self.l_score, self.r_score = 0, 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=203)
        self.write(f"{self.p1}: {self.l_score}", align="center", font=("courier", 16, "bold"))
        self.goto(x=100, y=203)
        self.write(f"{self.p2}: {self.r_score}", align="center", font=("courier", 16, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        game_over = False
        player = None
        if self.l_score == 5:
            player = self.p1
            game_over = True
        elif self.r_score == 5:
            player = self.p2
            game_over = True
        if game_over:
            draw_line(x=0, y=200, stop=-400, angle=270, draw=False)
            self.goto(0, -100)
            self.color("grey")
            self.write(f"{player} won the game. Press 'r' to restart.", align="center", font=("courier", 12, "bold"))
        return game_over
