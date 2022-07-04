from turtle import *
i=5
# super fast
speed(0)
while True:
    circle(i,i)
    left(60)
    i=i+5
    if i>1000:
        break