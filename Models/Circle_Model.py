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

    def MoveTo(self, x_loc,y_loc):
        self.Move = pygame.Rect.move(self,x_loc,y_loc)


    def Move_Y(self,y_loc):
        self.Location[1] = self.Location[1] + y_loc
    def Move_X(self,x_loc):
        self.Location[0] = self.Location[0] + x_loc

    
    def Rotate(self,angle):
         pygame.transform.rotate(self, angle)
    
    def SetSize(self, size):
        self.Size = size
        if self.Size < 0:
            self.Size = 0

    def ChangeSize(self, change):
        self.Size = self.Size + change
        if self.Size < 0 :
            self.Size = 0