from turtle import *
#pentagon
speed('slowest')
pencolor('red')
sides=5
for i in range(sides):
    forward(75)
    left(360/sides)
    dot(30,'blue')
mainloop()