import pygame


class Circle:

    def __init__(self,size,color:tuple,location:tuple,__defaultSurface):
        self.__BaseSetup(size,color,location,__defaultSurface)
        

    def __BaseSetup(self,size,color:tuple,location:tuple,__defaultSurface):
        self.Size = size
        self.Color = color
        self.Location = location
        self.__DefaultSurface = __defaultSurface
        self.Visible = True
        
    def ToggleVisibility(self):
        self.Visible = not self.Visible
    def Display(self):
        pygame.draw.circle(self.__DefaultSurface,self.Color,self.Location,self.Size)

    def MoveTo(self, x_loc,y_loc):
        self.Location = (x_loc,y_loc)


    def Move_Y(self,change):
        self.MoveTo(self.Location[0],self.Location[1] + change)
    def Move_X(self,change):
        self.MoveTo(self.Location[0] + change,self.Location[1])

    
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
    def ChangeDefaultSpeed(self, change):
        self.DefaultSpeed = self.DefaultSpeed + change
        if self.DefaultSpeed < 0:
            self.DefaultSpeed = 0