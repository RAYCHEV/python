import turtle

turtle.speed('fastest')
side_size = 10
angle = 74

for i in range(1,1000):
    turtle.forward(side_size)
    turtle.left(int(angle))
    side_size += 1

turtle.exitonclick()
