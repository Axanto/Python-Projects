from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        # the starting snake consists of 3 square so using mutable tuple, starting coordinates are stable
        self.segment = []  # segment list is for objects of snake's body
        self.create_snake()
        self.head = self.segment[0]
        self.head_mod()


    def create_snake(self):
        for position in STARTING_POSITION:  # for loop has used to create body in a row
            self.add_segment(position)

    def head_mod(self):
        self.head.color("#FEC260")
        self.head.shape("triangle")
        self.head.shapesize(0.8,0.8)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("#3FA796")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.setpos(position)
        self.segment.append(new_segment)  # appended to the segment list

    def extend(self):
        """ add a new segment to the snake """
        self.add_segment(self.segment[-1].pos())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):  # stop value is exclude!!!
            # In this loop each segment is replace its location with the next segment
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """ everything inside the init. Initalize the snake again."""
        for seg in self.segment:
            seg.goto(1000,1000)
        self.__init__()


    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


