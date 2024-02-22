from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor()< -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295 :
        score.reset()
        snake.reset_snake()
        
        

    for segment in snake.segment[1:]:
        if snake.head.distance(segment)< 10:
            score.reset()
            snake.reset_snake()
            
    
screen.exitonclick()
