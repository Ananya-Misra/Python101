import pgzrun 
HEIGHT=500
WIDTH=600


p=Rect((400,400),(50,50))
def draw():
    screen.fill('white')
    screen.draw.filled_rect(p,'blue')

# #after update draw is called
def update():
    control_player()
def control_player():
    if keyboard.RIGHT:
        p.x+=2
    if keyboard.LEFT:
        p.x+=-2
    if keyboard.UP:
        p.y+=-2
    if keyboard.DOWN:
        p.y+=2
pgzrun.go()
