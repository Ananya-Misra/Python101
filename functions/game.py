import pgzrun 
HEIGHT=400
WIDTH=600

background = Actor("background")
player = Actor("alien")
player.x = 200
player.y = 200
enemy = Actor("enemy",pos=(350,350))
def draw():
    screen.clear()
    screen.blit('background',(0,0))
    # background.draw()
    player.draw()
    enemy.draw()

def player_move():
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0
def enemy_move():
    if enemy.x>player.x:
        enemy.x-=1
    if enemy.x<player.x:
        enemy.x+=1
    if enemy.y>player.y:
        enemy.y-=1
    if enemy.y<player.y:
        enemy.y+=1
    if enemy.colliderect(player):
        player.image='splat'
    
def playerlimit_check():
    if player.x<0:
        player.x=WIDTH
    if player.x>WIDTH:
        player.x=0
    if player.y<0:
        player.y=HEIGHT
    if player.y>HEIGHT:
        player.y=0

def update():
    enemy_move()

        # sounds.splat.play()
    player_move()
    playerlimit_check()
   


    #player movement
        
pgzrun.go()