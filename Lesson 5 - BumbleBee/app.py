from random import randint
import pgzrun

WIDTH=400
HEIGHT=400
TITLE="Bee Game"

score=0
game_over = False

bee=Actor("bee")
bee.pos=100,100

flower = Actor("flower")
flower.pos = 200, 200

def draw():
  screen.blit("background",(0,0))
  bee.draw()
  flower.draw()
  screen.draw.text("Score : "+str(score), color="black",topleft=(10, 10))
  if game_over:
    screen.fill("pink")
    screen.draw.text("Time's Up ! Your Final Score :" + str(score), color="black",midtop=(WIDTH / 2, 10))

def place_flower():
  flower.x=randint(50,350)
  flower.y=randint(50,350)


def update():
  global score

  if keyboard.left: #keyboard.d (aswd key works)
    bee.x=bee.x-2
  if keyboard.right:
    bee.x=bee.x+2
  if keyboard.up:
    bee.y=bee.y-2
  if keyboard.down:
    bee.y=bee.y+2

  #True - if collision happens
  #false- if collision does not happen
  if bee.colliderect(flower):
    score=score+10
    place_flower()

def time_up():
  global game_over
  game_over=True

clock.schedule(time_up, 60.0)
place_flower()
pgzrun.go()
