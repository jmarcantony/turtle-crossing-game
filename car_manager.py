import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.setheading(180)
        new_car.penup()
        new_car.turtlesize(stretch_wid=2, stretch_len=4)
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-230, 230))
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def get_car(self):
        for car in self.all_cars:
            return car

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
