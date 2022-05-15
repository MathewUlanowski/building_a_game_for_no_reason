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
        config = Configuration("./settings.json")
        self.Surface = Screen(config.window_dimensions,config.background_color,"Boring Game")
        self.Height = config.window_dimensions[1]
        self.Width = config.window_dimensions[0]
        self.main_schema = Load_Schema("./Assets/Resources/Colors/Main")

    # the logic for what is ran each loop
    def RunGameTick(self):
        self.Surface.refresh()
        self.Key_Event_Handler()
        self.Surface.Update()

    