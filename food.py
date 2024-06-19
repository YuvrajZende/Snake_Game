import random
from turtle import Turtle


class Food:
    # this will generate the food on the screen
    def __init__(self):
        self.food = Turtle("circle")
        self.food.color("red")
        self.food.penup()
        self.regenerate()

    # it will regenerate the food for the snake after the collision
    def regenerate(self):
        x_axis = random.randint(-380, 380)
        y_axis = random.randint(-280, 280)
        self.food.goto(x_axis, y_axis)
