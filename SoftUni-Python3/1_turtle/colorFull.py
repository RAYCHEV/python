import turtle
import random

turtle.speed('fastest')


side_size = 10
angle = 74

turtle.colormode(255)
turtle.bgcolor('black')
for side_size in range(10,510):

    turtle.pencolor(random.randrange(side_size//4, 255 - side_size//4),
                    random.randrange(side_size//4, 255 - side_size//4),
                    random.randrange(side_size//4, 255 - side_size//4))
    turtle.forward(side_size)
    turtle.left(int(angle))
    print(side_size)

turtle.done()