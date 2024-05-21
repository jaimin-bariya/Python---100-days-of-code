from turtle import Turtle
import random
import time

COLORS = [
    "red", "green", "blue", "yellow", "black", "white",
    "purple", "orange", "pink", "brown", "gray", "cyan",
    "magenta", "lime", "maroon", "navy", "olive", "teal",
    "aqua", "silver", "gold", "indigo", "violet", "turquoise",
    "lavender", "beige", "coral", "khaki", "orchid", "salmon"
]
DISTANCE_BETWEEN_CARS = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.all_cars = []

    def createCar(self):
        random_num = random.randint(1,6)

        if random_num == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            
            # position of new generated car
            new_y = random.randint(-200, 200)
            new_car.goto(x=300, y=new_y)
            self.all_cars.append(new_car)

    def moveCars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)




    


