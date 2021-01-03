from turtle import Turtle
turtle_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
Up =90
Down = 270
Right = 0
Left = 180
class Snake:
    def __init__(self):
        self.turtle_list=[]
        self.create_snake()
        self.head = self.turtle_list[0]
    def create_snake(self):
        for position in turtle_pos:
           self.add_segment(position)
    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)
    def reset(self):
        for turt in self.turtle_list:
            turt.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]
    def extend(self):
        self.add_segment(self.turtle_list[-1].position())
    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle_num - 1].xcor()
            new_y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(new_x, new_y)
        self.head.forward(move_distance)
    def Up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)
    def Down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)
    def Left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)
    def Right(self):
        if self.head.heading() != Left:
            self.head.setheading(0)