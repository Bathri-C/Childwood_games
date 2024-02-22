from turtle import Turtle,Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
      def __init__(self):
        
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
      def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add(position)
            
      def add(self,position):
          tom=Turtle("square")
          tom.color("white")
          tom.penup()
          tom.goto(position)
          self.segment.append(tom)

      def reset_snake(self):
          for segment  in self.segment:
              segment.goto(1000,1000)
          self.segment.clear()
          self.create_snake()
          self.head=self.segment[0]
      
      def extend(self):
          self.add(self.segment[-1].position())
          
      def move(self):
        for seg in range(len(self.segment)-1,0,-1):
                new_x=self.segment[seg-1].xcor()
                new_y=self.segment[seg-1].ycor()
                self.segment[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
      def up(self):
          if self.head.heading()!=DOWN:
              self.head.setheading(UP)
      def down(self):
          if self.head.heading()!=UP:
              self.head.setheading(DOWN)
      def left(self):
          if self.head.heading()!=RIGHT:
              self.head.setheading(LEFT)
      def right(self):
          if self.head.heading()!=LEFT:
              self.head.setheading(RIGHT)
          