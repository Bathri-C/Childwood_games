from turtle import Turtle
from snake import Snake
from food import Food
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            data_int=int(data.read())
            self.highscore=data_int
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"score : {self.score}  highscore : {self.highscore}",align="center",font=("Courier",18,"normal"))
        self.hideturtle()

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")

        self.score=0
        self.clear()
        self.write(f"score : {self.score}  highscore : {self.highscore}",align="center",font=("Courier",18,"normal"))


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over.",align="center",font=("Courier",18,"normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"score : {self.score}  highscore : {self.highscore}",align="center",font=("Courier",18,"normal"))

