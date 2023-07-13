from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.segment = []
        self.make_snake()

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def snake_up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(90)

    def snake_down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(270)

    def snake_left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(180)

    def snake_right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(0)

    def move_snake(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

