#pentagon with circle
from turtle import *
pensize(18) #determines thickness of the pen
fillcolor('red')
begin_fill()
for i in range(5):
    fd(100)
    lt(72)
end_fill()
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()

mainloop()