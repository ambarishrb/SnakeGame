from turtle import Turtle
MOVE_DISTANCE = 10


class Snake:
    def __init__(self):
        self.STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
        self.segments = []
        self.create()
        self.head = self.segments[0]


    def create(self):
        for position in self.STARTING_POSITIONS:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.setposition(position)
            self.segments.append(t)

    def extend(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.setposition(self.segments[-1].position())
        self.segments.append(t)


    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[segment - 1].xcor()
            y_cord = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cord, y_cord)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
