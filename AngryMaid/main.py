import pygame as pg
import sys

from scripts.Scenes.Game.game import Dialogue
from scripts.Scenes.MainMenu.mainMenu import Menu
from scripts.Scenes.DrawScreen.catchMe import FallingGame
from scripts.Music.musicPlayer import Music
pg.init() #initialize pygame window

#ICON
pygame_icon = pg.image.load('assets/ui/icons/icon.png')
pg.display.set_icon(pygame_icon)
pg.display.set_caption("Angry Maid")

# Create a screen with the specified dimensions
screen = pg.display.set_mode((800,  600))


mS = Music()


'''---------------------------------------------------------------------------------------------------------'''

# Create an instance of the Menu class, passing the screen and button images to it
mS.pickMusic("mainMenu")
mS.play()

menu = Menu(screen)
menu.main() # Run the main function of the menu

#Dialogue
mS.pickMusic("dialogue")
mS.play()

dial = Dialogue(screen)
dial.dialogueSys.start_dialogue()
dial.run()

#Falling Game
mS.pickMusic("game3")
mS.play()

gameFall = FallingGame()
gameFall.run()

# Quit pygame when the loop is finished
pg.quit()
sys.exit()