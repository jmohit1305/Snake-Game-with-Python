from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        snake_turtle = Turtle("square")
        snake_turtle.color("white")
        snake_turtle.penup()
        snake_turtle.goto(position)
        self.segments.append(snake_turtle)

    def increase_length(self):
        new_position = self.segments[-1].position()
        self.add_segment(new_position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_x = self.segments[seg_num - 1].xcor()
            seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(seg_x, seg_y)

        self.head.forward(MOVE_DISTANCE)

    def current_position(self):
        return self.head.position()

    def snake_direction(self, cor1, cor2):
        if self.head.heading() != cor1:
            self.head.setheading(cor2)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        self.snake_direction(cor1=DOWN, cor2=UP)

    def down(self):
        self.snake_direction(cor1=UP, cor2=DOWN)

    def left(self):
        self.snake_direction(cor1=RIGHT, cor2=LEFT)

    def right(self):
        self.snake_direction(cor1=LEFT, cor2=RIGHT)
