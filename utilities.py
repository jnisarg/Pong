import time
from turtle import Turtle, Screen


def refactor_names(*args):
    names = []
    for name in args:
        if name:
            name = name.strip()
            name = name.capitalize()
        names.append(name)
    return tuple(names)


def get_players():
    screen = Screen()
    p1 = screen.textinput(title="Player 1", prompt="Enter name of Player 1: ")
    p2 = screen.textinput(title="Player 2", prompt="Enter name of Player 2: ")
    p1, p2 = refactor_names(p1, p2)
    return (p1, p2) if p1 and p2 else ("P1", "P2")


def draw_line(x=0, y=0, stop=0, angle=0, vertical=True, color="white", style="dashed", draw=True):
    def move():
        line.down()
        line.fd(1)
        if style == "dashed":
            line.up()
            line.fd(10)
    line = Turtle()
    line.hideturtle()
    line.up()
    line.speed(0)
    line.goto(x, y)
    line.seth(angle)
    if draw:
        line.color(color)
    if vertical:
        if stop < y:
            while line.ycor() >= stop:
                move()
        else:
            while line.ycor() <= stop:
                move()
    else:
        if stop < x:
            while line.xcor() >= stop:
                move()
        else:
            while line.xcor() <= stop:
                move()


def new_round():
    turtle = Turtle()
    turtle.color("orange")
    turtle.hideturtle()
    turtle.goto(0, -100)
    draw_line(x=0, y=200, stop=-400, angle=270, draw=False)
    for i in range(3, -1, -1):
        turtle.clear()
        turtle.write(f"New round will begin in: {i}", align="center", font=("courier", 12, "bold"))
        time.sleep(1)
    turtle.clear()
    draw_line(x=0, y=200, stop=-400, angle=270)


def game_graphics():
    x, y = 400, 400
    for _ in range(10):
        draw_line(x=x, y=200, stop=-400, angle=270, color="yellow", style="solid")
        draw_line(x=-x, y=200, stop=-400, angle=270, color="yellow", style="solid")
        x += 1
    for _ in range(30):
        draw_line(x=-409, y=-y, stop=409, angle=0, vertical=False, color="yellow", style="solid")
        draw_line(x=-409, y=y-200, stop=-309, angle=0, vertical=False, color="yellow", style="solid")
        draw_line(x=309, y=y-200, stop=409, angle=0, vertical=False, color="yellow", style="solid")
        y += 1
    draw_line(x=-409, y=229, stop=409, angle=0, vertical=False, color="yellow", style="solid")
    draw_line(x=-409, y=200, stop=409, angle=0, vertical=False, color="yellow", style="solid")
    draw_line(x=0, y=229, stop=200, angle=270, color="yellow", style="solid")
    draw_line(x=0, y=200, stop=-400, angle=270)


pong = """
 ▄▄▄·       ▐ ▄  ▄▄ • 
▐█ ▄█▪     •█▌▐█▐█ ▀ ▪
 ██▀· ▄█▀▄ ▐█▐▐▌▄█ ▀█▄
▐█▪·•▐█▌.▐▌██▐█▌▐█▄▪▐█
.▀    ▀█▄▀▪▀▀ █▪·▀▀▀▀ 
"""


def print_logo():
    logo = Turtle()
    logo.up()
    logo.goto(0, 250)
    logo.hideturtle()
    logo.color("white")
    logo.write(pong, align="center", font=("courier", 24, "bold"))
