import pygame

class Rectangle:

    def __init__(self,rectsize,color:tuple,location:tuple,__defaultSurface):
        self.__baseSetup(rectsize,color,location,__defaultSurface)
        

    def __baseSetup(self,rectsize,color:tuple,location:tuple,__defaultSurface):
        self.RectSize = rectsize
        self.Color = color
        self.Location = location
        self.__DefaultSurface = __defaultSurface
        
    def Display(self):
        pygame.draw.rect(self.__DefaultSurface,self.color,self.RectSize)

    def MoveTo(self,moveX:tuple,moveY:tuple):
        self.Move = pygame.Rect.move(self,moveX,moveY)

    def Move_Y(self,moveY):
        self.Location[1] = self.Location[1] + moveY
    def Move_X(self,moveX):
        self.Location[0] = self.Location[0] + moveX

    def Rotate(self,angle):
         pygame.transform.rotate(self, angle)