from copyreg import constructor
import pygame
from Controllers.Colors.Color_Loader_Controller import *
from Controllers.Game_Controller import Game

def GameLoop():
    # initialization of the game and assignment to a variable
    game = Game()

    # main Game loop
    while game.Run_Condition:
        game.RunGameTick()

    pygame.quit()
    print("thank you for playing.")
