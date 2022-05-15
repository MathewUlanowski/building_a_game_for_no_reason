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

    def ToggleVisibility(self):
        self.Visible = not self.Visible

    def MoveTo(self, moveX,moveY):
        self.Move = pygame.Rect.move(self,moveX,moveY)
    def Move_Y(self,moveY):
        self.Location[1] = self.Location[1] + moveY
    def Move_X(self,moveX):
        self.Location[0] = self.Location[0] + moveX
    
    def SetLength(self, startL,endL):
        self.StartL = startL
        self.EndL = endL
        if self.StartL | self.EndL < 0:
            self.StartL = 0
            self.endL = 0
    def ChangeLength(self, change):
        self.EndL = self.EndL + change
        if self.EndL < 0 :
            self.EndL = 0