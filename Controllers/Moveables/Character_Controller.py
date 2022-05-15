import pygame
from Models.Shapes.Circle_Model import Circle


class Character(Circle):
    def __init__(self, size, color: tuple, location: tuple, __defaultSurface,x_bounds,y_bounds):
        super().__init__(size, color, location, __defaultSurface)
        self.XMomentum = 0
        self.YMomentum = 0
        self.XBounds = x_bounds
        self.YBounds = y_bounds
        self.DefaultSpeed = 1

    def Run(self):
        self.Travel()
        self.RepelBoundry(100)


    def Travel(self):
        self.Move_X(self.XMomentum)
        if self.Location[0]<self.XBounds[0]:
            self.Location = (0,self.Location[1])
        if self.Location[0]>self.XBounds[1]:
            self.Location = (self.XBounds[1],self.Location[1])

        self.Move_Y(self.YMomentum)
        if self.Location[1]<self.YBounds[0]:
            self.Location = (self.Location[0],0)
        if self.Location[1]>self.YBounds[1]:
            self.Location = (self.Location[0],self.YBounds[1])
    
    def AccelerateX(self,change):
        self.XMomentum += change
    def AccelerateY(self,change):
        self.YMomentum += change





    def RepelBoundry(self,padding):
        if self.Location[0] < self.XBounds[0]+padding:
            self.AccelerateX(0.1)
            pass
        if self.Location[0] > self.XBounds[1]-padding:
            self.AccelerateX(-0.1)
            pass
        if self.Location[1] < self.YBounds[0]+padding:
            self.AccelerateY(0.1)
            pass
        if self.Location[1] > self.YBounds[1]-padding:
            self.AccelerateY(-0.1)
            pass