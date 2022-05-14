from matplotlib.backend_bases import LocationEvent
import pygame


class Circle:

    def __init__(self,size,color:tuple):
        self.__baseSetup(size,color)
    def __init__(self,size,color:tuple,location:tuple):
        self.__baseSetup(location)

    def __baseSetup(self,size,color:tuple,location:tuple):
        self.Size = size
        self.Color = color
        self.Location = location

    def moveTo(self, moveX:tuple,moveY:tuple):
        self.Move = pygame.Rect.move(self,moveX,moveY)
