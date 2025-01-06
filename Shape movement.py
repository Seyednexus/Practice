# Ahmadreza Elyasi & Mir Muhammad Seyyedghasemi#

import turtle
import random
import math

class Shape:
    def __init__(self):
        self.shape_type = random.choice(['triangle', 'square', 'rectangle'])
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.shape("square")  
        self.turtle.shapesize(1, 1)
        self.turtle.color((random.random(), random.random(), random.random()))
        self.turtle.speed(0)
        self.turtle.goto(random.randint(-300, 300), random.randint(-250, 250))
        self.speed_x = random.choice([-1, 1])
        self.speed_y = random.choice([-1, 1])
        while self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = random.choice([-1, 1])
            self.speed_y = random.choice([-1, 1])
        self.update_shape()

    def update_shape(self):
        if self.shape_type == 'triangle':
            self.turtle.shape("triangle")
        elif self.shape_type == 'square':
            self.turtle.shape("square")
        elif self.shape_type == 'rectangle':
            self.turtle.shape("square")
            self.turtle.shapesize(1, 2)

    def move(self):
        self.turtle.setx(self.turtle.xcor() + self.speed_x)
        self.turtle.sety(self.turtle.ycor() + self.speed_y)

        if self.turtle.xcor() < -400 or self.turtle.xcor() > 400:
            self.speed_x *= -1
        if self.turtle.ycor() < -300 or self.turtle.ycor() > 300:
            self.speed_y *= -1

    def check_collision(self, other):
        distance = math.sqrt((self.turtle.xcor() - other.turtle.xcor()) ** 2 + (self.turtle.ycor() - other.turtle.ycor()) ** 2)
        return distance < 20


window = turtle.Screen()
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0) 

shapes = []


num_shapes = 20


for _ in range(num_shapes):
    shapes.append(Shape())


while True:
    for shape in shapes:
        shape.move()


    for i in range(len(shapes) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if shapes[i].check_collision(shapes[j]):
                if shapes[i].shape_type == shapes[j].shape_type:
                    shapes[i].speed_x *= -1
                    shapes[i].speed_y *= -1
                    shapes[j].speed_x *= -1
                    shapes[j].speed_y *= -1
                else:
                    shapes[i].turtle.hideturtle()
                    new_shape_type = random.choice(['triangle', 'square', 'rectangle'])
                    shapes[j].shape_type = new_shape_type
                    shapes[j].update_shape()
                    shapes.pop(i)
                    break

    window.update()
