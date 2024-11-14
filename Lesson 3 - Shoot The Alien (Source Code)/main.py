import pgzrun
from random import randint

#Python standard for deciding the title of the window
TITLE="Shoot the Alien"

#Python standard for deciding the Width and height of the window
WIDTH=400
HEIGHT=400

#global variable - access this anywhere in the program
message="Game Starts.."

#Actor- in built Object 
alien=Actor('alien')
alien.pos=50,50

def draw():
  screen.clear()
  screen.fill(color="brown")
  alien.draw()
  screen.draw.text(message, center=(200,20), fontsize=30, color="black")


#User defined function to place alien at random position
def place_alien():
  alien.x=randint(50,350)
  alien.y=randint(50,350)

#on_mouse_down - in built function which gets triggered, when you click on the game screen
def on_mouse_down(pos):
  print("Hi ! ")
  global message
  #collidepoint - inbuilt function - checks collision between mouse pointer and actor
  if alien.collidepoint(pos):
    message="Good Shot !"
    place_alien()
  else:
    message="You missed it. Try again !"

place_alien()
pgzrun.go()
