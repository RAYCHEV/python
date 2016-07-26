import turtle
import time

turtle.speed("fastest")
turtle.setup(380, 380)

x = -160
y = 160
side=40
for ii in range(8):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for i in range(8):
        if i % 2==0 and ii % 2 == 0:
            turtle.begin_fill()
        if not i % 2 == 0 and not ii % 2 == 0:
            turtle.begin_fill()

        for sq in range(4):
            turtle.forward(side)
            turtle.right(90)

        turtle.end_fill()
        turtle.forward(side)
    y -= 40

time.sleep(10) # delay a few sec before a windows will be close