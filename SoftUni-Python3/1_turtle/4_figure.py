import turtle

side_size = ""
angle = ""
while not side_size.isdigit():
    side_size = input('Enter a side size: ').strip()

while not angle.isdigit():
    angle = input("Enter a angle: ").strip()

side_size_int = int(side_size)
while True:
    turtle.forward(side_size_int)
    turtle.left(int(angle))
    side_size_int += 1

turtle.done()