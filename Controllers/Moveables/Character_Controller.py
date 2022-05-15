import pygame
from Models.Shapes.Circle_Model import Circle


class Character(Circle):
    def __init__(self, size, color: tuple, location: tuple, __defaultSurface):
        super().__init__(size, color, location, __defaultSurface)
        self.XMomentum = 0
        self.YMomentum = 0

    def Run(self):
        
        self.Travel()

    def Travel(self):
        self.Move_X(self.XMomentum)
        self.Move_Y(self.YMomentum)
    
    def AccelerateX(self,change):
        self.XMomentum += change
    def AccelerateY(self,change):
        self.YMomentum += change