import pygame

from Models.Shapes.Shape_Base_Model import ShapeBase

class Square(ShapeBase):
    def __init__(self, size, color: tuple, location: tuple,surface) -> None:
        super().__init__(size, color, location)
        self.__DefaultSurface = surface
        
    def Display(self):
        pygame.draw.rect(self.__DefaultSurface,self.Color,pygame.Rect(self.Location[0] - self.Size/2,self.Location[1] - self.Size/2,self.Size,self.Size))

    def Rotate(self,angle):
         pygame.transform.rotate(self, angle)