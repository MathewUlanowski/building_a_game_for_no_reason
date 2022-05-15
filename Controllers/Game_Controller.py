from turtle import width
import pygame
from Controllers.Colors.Color_Loader_Controller import Load_Schema
from Controllers.Event_Controller import EventController
from Controllers.Moveables.Character_Controller import Character
from Models.Main.Screen_Model import Screen
from Models.Main.Config import Configuration
from Models.Shapes.Circle_Model import Circle
from Models.Shapes.Rect_Model import Rectangle


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
        self.TestCircle = Character(
            20,
            self.Main_schema.GetPalette("Warm-Autumn").GetColor("Catawba"),
            (self.Width/2,self.Height/2),
            self.Surface.Window
            )

    # the logic for what is ran each loop
    def RunGameTick(self):
        self.GameClock.tick(self.FrameRate)
        self.Surface.refresh()
        self.Key_Event_Handler()

        # some testing to move stuff based on inputs
        

        if self.IsToggled(pygame.K_a):
            self.TestCircle.AccelerateX(-self.TestCircle.DefaultSpeed)
        if self.IsToggled(pygame.K_d):
            self.TestCircle.AccelerateX(self.TestCircle.DefaultSpeed)
        if self.IsToggled(pygame.K_w):
            self.TestCircle.AccelerateY(-self.TestCircle.DefaultSpeed)
        if self.IsToggled(pygame.K_s):
            self.TestCircle.AccelerateY(self.TestCircle.DefaultSpeed)
        if self.IsToggled(pygame.K_UP):
            self.TestCircle.ChangeDefaultSpeed(0.1)
        if self.IsToggled(pygame.K_DOWN):
            self.TestCircle.ChangeDefaultSpeed(-0.1)
        if self.IsToggled(pygame.K_SPACE):
            pass
        
        self.TestCircle.Travel()

        if self.IsToggled(pygame.K_ESCAPE):
            self.QuitGame()
        
        
        self.TestCircle.Display()
        self.Surface.Update()

    