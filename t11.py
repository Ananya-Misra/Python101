#shell shape
from turtle import *
pencolor('blue')
speed('fastest')
pensize(4)
fillcolor('red')
for i in range(10,0,-1):
   begin_fill()
   circle(i*10)
   lt(25)
   end_fill()
goto(20,250)
mainloop()
