from msilib.schema import Class
import pygame

class Line:

    def __init__(self,__defaultSurface, color:tuple,startL,endL,width):
        self.__BaseSetup(__defaultSurface,color,startL,endL,width)

    def __BaseSetup(self, __defaultSurface,color:tuple,startL,endL,width):
        self.__DefaultSurface = __defaultSurface
        self.Color = color
        self.StartL = startL
        self.EndL = endL
        self.Width = width
        self.Visible = True

    def Display(self):
        if self.Visible:
            pygame.draw.line(self.__DefaultSurface,self.Color,self.StartL,self.EndL,self.Width)

    def SetStart(self, start_point: tuple):
        self.StartL = start_point
    def SetEnd(self, end_point:tuple):
        self.EndL = end_point

    def ToggleVisibility(self):
        self.Visible = not self.Visible
    