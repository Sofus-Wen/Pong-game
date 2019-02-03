import turtle
import winsound

winsound.PlaySound("01-main-theme-overworld.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC)

wn = turtle.Screen()
wn.title("Pong Turtle Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
Point_A = 0
Point_B = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1 = {} Player 2 = {}".format(Point_A, Point_B), align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y_a = paddle_a.ycor()
    y_a += 40
    paddle_a.sety(y_a)


def paddle_a_down():
    y_a = paddle_a.ycor()
    y_a -= 40
    paddle_a.sety(y_a)


def paddle_b_up():
    y_b = paddle_b.ycor()
    y_b += 40
    paddle_b.sety(y_b)


def paddle_b_down():
    y_b = paddle_b.ycor()
    y_b -= 40
    paddle_b.sety(y_b)


def Winnerscreen_1():
    wn = turtle.Screen()
    wn.title("Player 1 Won!!!")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Player 1 Won!!", align="center", font=("Courier", 65, "normal"))


def Winnerscreen_2():
    wn = turtle.Screen()
    wn.title("Player 2 Won!!!")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Player 2 Won!!", align="center", font=("Courier", 65, "normal"))


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w".lower())
wn.onkeypress(paddle_a_down, "s".lower())
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

player_1 = input("What should i call u(1): ")
player_2 = input("What should i call u(2): ")


# Mainloop
while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking(Ball bounce)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("331381__qubodup__public-domain-jump-sound.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("331381__qubodup__public-domain-jump-sound.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        Point_B += 1
        ball.dx *= -1
        pen.clear()
        pen.write("{} = {} {} = {}".format(player_1, Point_A, player_2, Point_B), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 390:
        ball.goto(0, 0)
        Point_A += 1
        ball.dx *= -1
        pen.clear()
        pen.write("{} = {} {} = {}".format(player_1, Point_A, player_2, Point_B), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if 340 < ball.xcor() < 350 and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("331381__qubodup__public-domain-jump-sound.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if -340 > ball.xcor() > -350 and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("331381__qubodup__public-domain-jump-sound.wav", winsound.SND_ASYNC)

    if Point_A == 10:
        print("{} Won!!!".format(player_1))
        False
        Winnerscreen_1()

    if Point_B == 10:
        print("{} Won!!!".format(player_2))
        False
        Winnerscreen_2()
