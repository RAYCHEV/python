import turtle

g = 134
l = 120
i=""

while not i.isdigit():
    i = input('Enter count iterations: ').strip()

i = int(i)
for ii in range(0, i):
    turtle.left(g)
    turtle.forward(l)
    print(ii)

turtle.done()
