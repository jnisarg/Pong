import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from utilities import game_graphics, print_logo


def pong():
    screen = Screen()
    screen.setup(width=900, height=1000)
    screen.bgcolor("black")
    screen.title("Pong: The Famous Arcade Game")
    screen.tracer(0)

    print_logo()

    l_paddle = Paddle((-380, -100))
    r_paddle = Paddle((380, -100))

    ball = Ball()

    scoreboard = ScoreBoard()

    game_graphics()

    def restart():
        screen.clear()
        pong()

    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    screen.onkey(restart, "r")

    game_off = False
    while not game_off:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 180 or ball.ycor() < -380:
            ball.bounce_y()

        if (ball.distance(r_paddle) < 50 and ball.xcor() > 355) or (ball.distance(l_paddle) < 50 and ball.xcor() < -355):
            ball.bounce_x()

        if ball.xcor() > 395:
            ball.refresh()
            l_paddle.refresh()
            r_paddle.refresh()
            scoreboard.l_point()

        if ball.xcor() < -395:
            ball.refresh()
            l_paddle.refresh()
            r_paddle.refresh()
            scoreboard.r_point()

        game_off = scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    pong()
