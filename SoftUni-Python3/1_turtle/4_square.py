import turtle

side_size = ""
while not side_size.isdigit():
    side_size = input('Enter a number: ').strip()

for i in range(4):
    turtle.forward(int(side_size))
    turtle.left(90)

turtle.done()
