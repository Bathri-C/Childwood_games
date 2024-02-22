from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Score
import time

screen=Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong_Game")
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
ball=Ball()
score=Score()
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

    
        



    


screen.exitonclick()
