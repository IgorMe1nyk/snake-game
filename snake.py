from turtle import Turtle
X_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]


    def create_snake(self):
        for n in X_POSITIONS:
            self.add_square(n)

    def add_square(self, n):
        square = Turtle(shape="square")
        square.penup()
        square.color("white")
        square.goto(n)
        self.all_squares.append(square)

    def extend(self):
        self.add_square(self.all_squares[-1].position())


    def move(self):
        for square_number in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[square_number - 1].xcor()
            new_y = self.all_squares[square_number - 1].ycor()
            self.all_squares[square_number].goto(new_x, new_y)
        self.all_squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)







