from turtle import width
import pygame
from Controllers.Colors.Color_Loader_Controller import Load_Schema
from Controllers.Keys.Event_Controller import EventController
from Models.Main.Screen_Model import Screen
from Models.Main.Config import Configuration
from Models.Circle_Model import Circle


class Game(EventController):
    def __init__(self):
        EventController.__init__(self)
        pygame.init()
        # pygame.joystick.init()
        config = Configuration()
        self.Surface = Screen(config.WindowDimensions,config.BackgroundColor,"Boring Game")
        self.Height = config.WindowDimensions[1]
        self.Width = config.WindowDimensions[0]
        self.FrameRate = config.FrameRate
        self.Main_schema = Load_Schema("./Assets/Resources/Colors/Main")
        self.GameClock = pygame.time.Clock()

    # the logic for what is ran each loop
    def RunGameTick(self):
        self.GameClock.tick(self.FrameRate)
        self.Surface.refresh()
        self.Key_Event_Handler()
        self.Surface.Update()

    