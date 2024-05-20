from turtle import Turtle

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)



    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)



    def extend(self):
        self.add_segment(self.segments[-1].position())
        
        
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_cor = self.segments[seg_num-1].position()
            
            self.segments[seg_num].goto(new_cor)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


    # check collision with wall
    def checkCollisionWall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        
    # check collision with tail
    def checkCollisionTail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
    
        

