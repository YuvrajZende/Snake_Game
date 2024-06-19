from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.extend_snake(position)

    def extend_snake(self, position):
        t = Turtle('square')
        t.penup()
        t.color("white")
        t.goto(position)
        self.segment.append(t)

    def extent(self):
        self.extend_snake(self.segment[-1].position())

    def move(self):  # allow the snake to move in the dimension
        for seg in range(len(self.segment) - 1, 0, -1):
            x_axis = self.segment[seg - 1].xcor()
            y_axis = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x_axis, y_axis)
        self.head.forward(20)

    # controls of the snake on the keyboard
    def up(self):
        if self.head.heading() != 270:  # this if is written because the snake should not move 180 degrees
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
