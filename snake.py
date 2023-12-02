move_dis = 20
up = 90
down = 270
left = 180
right = 0
starting_positions = [(0,0),(-20,0),(-40,0)]
import turtle as t
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in starting_positions:
            self.add_segment(i)

    def move(self):
        for seg_no in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_no-1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x,new_y)
        self.head.forward(move_dis)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,i):
        snake = t.Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(i)
        self.segments.append(snake)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)