from turtle import *
colors=['red','blue','green','yellow','purple','orange']
speed('fastest')
s=len(colors)
for i in range(500):
    c=colors[i%s]
    pencolor(c)
    forward(i+5)
    left(360/s)
    for j in range(s):
        forward(100)
        left(360/s)
mainloop()