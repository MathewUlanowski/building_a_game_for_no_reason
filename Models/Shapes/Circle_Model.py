import pygame

from Models.Shapes.Shape_Base_Model import ShapeBase


class Circle(ShapeBase):

    def __init__(self, size, color: tuple, location: tuple, surface) -> None:
        super().__init__(size, color, location)
        self.__DefaultSurface = surface
    
    def Display(self):
        pygame.draw.circle(self.__DefaultSurface,self.Color,self.Location,self.Size)
    
    def Rotate(self,angle):
         pygame.transform.rotate(self, angle)
    
    

    
    