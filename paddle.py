from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.up()
        self.color("green")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 140:
            new_y = self.ycor() + 10
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() > -340:
            new_y = self.ycor() - 10
            self.goto(x=self.xcor(), y=new_y)

    def refresh(self):
        self.goto(self.position)
