#random flower design

from re import M
from turtle import *
import random
s=Screen()
s.setup(500,500)#screen setup l and h
speed(0)#godspeed
colors=['pink','orange']
for i in range(50):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    #select random pensize
    pensize(random.randint(1,2))
    pencolor(colors[random.randint(0,1)])
    radius=random.randint(5,30)
    fillcolor('red')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
mainloop()
