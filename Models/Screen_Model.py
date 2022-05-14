import pygame

class Screen:
    # constructor and overloads
    def __init__(self,dim: tuple,background: tuple):
        self.__baseSetup(dim,background)
        self.SetGameCaption("Untitled")
    def __init__(self,dim:tuple,background:tuple,caption):
        self.__baseSetup(dim,background)
        self.SetGameCaption(caption)


    def __baseSetup(self,dim:tuple,background:tuple):
        self.Dimensions = dim
        self.Background = background
        self.Window = pygame.display.set_mode(self.Dimensions)
    def refresh(self):
        self.Window.fill(self.Background)
    def SetGameCaption(self,caption):
        pygame.display.set_caption(caption)
    def Update(self):
        pygame.display.update()