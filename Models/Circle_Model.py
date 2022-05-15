import pygame


class Circle:

    def __init__(self,size,color:tuple,location:tuple,__defaultSurface):
        self.__BaseSetup(size,color,location,__defaultSurface)
        

    def __BaseSetup(self,size,color:tuple,location:tuple,__defaultSurface):
        self.Size = size
        self.Color = color
        self.Location = location
        self.__DefaultSurface = __defaultSurface
        
    def Display(self):
        pygame.draw.circle(self.__DefaultSurface,self.Color,self.Location,self.Size)

    def MoveTo(self, moveX:tuple,moveY:tuple):
        self.Move = pygame.Rect.move(self,moveX,moveY)


    def Move_Y(self,moveY):
        self.Location[1] = self.Location[1] + moveY
    def Move_X(self,moveX):
        self.Location[0] = self.Location[0] + moveX

    
    def Rotate(self,angle):
         pygame.transform.rotate(self, angle)
