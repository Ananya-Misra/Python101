import pgzrun
#window height and width
HEIGHT=500
WIDTH=500
#x,y,width,height
box=Rect(50,50,100,100)
box2=Rect(250,50,100,50)
box3=Rect((400,400),(50,50))
def draw():
    screen.fill('black')
    screen.draw.rect(box,'red')
    screen.draw.filled_rect(box2,'yellow')
    screen.draw.filled_rect(box3,'white')

pgzrun.go()