from turtle import *
shapesize(5,5)
side=6
for i in range(100):
    dot(90,'red')
    fd(100)
    lt(360/side)
    dot(90,'red')
    circle(90,180)# specifying the radius and the arc
mainloop()