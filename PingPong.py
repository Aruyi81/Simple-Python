import turtle

win = turtle.Screen()
win.title("Pong by CodeClicks")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A (Fixed size)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 100px tall
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)  # 120px tall
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Movement functions with boundary checks
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y > 240:  # Prevent going above top
        y = 240
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y < -240:  # Prevent going below bottom
        y = -240
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y > 240:
        y = 240
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y < -240:
        y = -240
    paddle_b.sety(y)


# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Score system
score_a = 0
score_b = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}",
                        align="center", font=("Courier", 24, "normal"))


# Game loop
def play():
    global score_a, score_b

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top/bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1  # Bounce

    # Scoring
    if ball.xcor() > 390:  # Right side
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        update_score()

    elif ball.xcor() < -390:  # Left side (fixed condition)
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        update_score()

    # Paddle collisions
    # Right paddle (B)
    if (340 < ball.xcor() < 350 and
            paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60):
        ball.color("blue")
        ball.dx *= -1

    # Left paddle (A)
    elif (-350 < ball.xcor() < -340 and
          paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.dx *= -1  # Fixed typo here

    win.update()
    win.ontimer(play, 20)  # 50 FPS


play()
turtle.mainloop()  # Changed from turtle.done()