import turtle

win = turtle.Screen()
win.title('Pong by Matheus')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)#stops the window from updating, speeds up the game

player_a = 0
player_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #maximum possible speed
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #maximum possible speed
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0) #maximum possible speed
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
#every time the ball moves it moves by two pixels (diagonal):
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() #don't want to draw a line
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 16, 'normal'))


#functions
def paddle_a_up():
    y  = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y  = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y  = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y  = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
win.listen() #listen for keyboard input
win.onkeypress(paddle_a_up,'w') #when the user presses w paddle a up
win.onkeypress(paddle_a_down,'s') #when the user presses s paddle a down
win.onkeypress(paddle_b_up,'Up') #when the user presses w paddle a up
win.onkeypress(paddle_b_down,'Down') #when the user presses s paddle a down


#main game loop
while (1):
    win.update()

    #move the ball:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking:
    if ball.ycor() > 290:
        ball.sety(290) #brings ball back to edge of the screen
        ball.dy *= -1  #reverses direction of ball

    if ball.ycor() < -290:
        ball.sety(-290) #brings ball back to edge of the screen
        ball.dy *= -1  #reverses direction of ball
    if ball.xcor() < -390:
        ball.goto(0, 0) #brings ball back to center
        ball.dx *= -1  #reverses direction of ball
        player_b += 1 #adds point to player
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(player_a, player_b), align='center', font=('Courier', 16, 'normal'))

    if ball.xcor() > 390:
        ball.goto(0, 0) #brings ball back to center
        ball.dx *= -1  #reverses direction of ball
        player_a += 1 #adds points to player
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(player_a, player_b), align='center', font=('Courier', 16, 'normal'))


    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 #bounce and change direction

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 #bounce and change direction
