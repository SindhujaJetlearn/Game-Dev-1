#Draw ship
#Draw enemy
#Draw bullet
#Ship movement
#bullet movement
#enemy movement
#game logic

import pgzrun

#screen dimensions
WIDTH = 1200
HEIGHT = 600

#definiting colours
WHITE = (255, 255, 255)

#create a ship
ship = Actor('ship')
bug = Actor('bug')

ship.pos = (WIDTH // 2, HEIGHT - 60)

speed = 5 #Ship speed

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

score = 0
direction = 1

ship.dead = False
ship.countdown = 90

for x in range(8):
  for y in range(4):
    enemies.append(Actor('bug'))
    enemies[-1].x = 100 + 50 * x  #150,200,250
    enemies[-1].y = 80 + 50 * y

def on_key_down(key):
  if ship.dead == False:
    if key == keys.SPACE:
      bullets.append(Actor('bullet'))
      bullets[-1].x = ship.x
      bullets[-1].y = ship.y

def gameOver():
  screen.draw.text("GAME OVER", (250, 300))

def update():
  global score
  global direction
  moveDown = False #enemy movement

  #ship movement
  if ship.dead==False:
    if keyboard.left:
      ship.x -= speed
      if ship.x <= 0:
        ship.x=0
    elif keyboard.right:
      ship.x += speed
      if ship.x >= WIDTH:
        ship.x=WIDTH

  #bullet Movement     
  for bullet in bullets:
    if bullet.y <=0:
      bullets.remove(bullet)
    #bullet moves up
    else:
      bullet.y -=10

  if len(enemies)>0  and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):
    moveDown = True
    direction = direction*-1

  for enemy in enemies:
    enemy.x += 5*direction
    if moveDown == True:
      enemy.y +=100
    if enemy.y >HEIGHT:
      enemies.remove(enemy)

    #bullet and enemy collision
    for bullet in bullets:
      if enemy.colliderect(bullet):
        score +=100
        bullets.remove(bullet)
        enemies.remove(enemy)
        if len(enemies) == 0:
          gameOver()

    #ship and enemy collision
    if enemy.colliderect(ship):
      ship.dead=True

  if ship.dead:
    ship.countdown -=1
  #respawning the ship
  if ship.countdown == 0:
    ship.dead = False
    ship.countdown = 90


def draw():
  screen.clear()
  screen.fill("cadetblue")
  screen.draw.text("Score:"+str(score), (50, 30))
  
  for bullet in bullets:
    bullet.draw()
  for enemy in enemies:
    enemy.draw()

  if ship.dead == False:
    ship.draw()

  if len(enemies) == 0:
    gameOver()


pgzrun.go()
