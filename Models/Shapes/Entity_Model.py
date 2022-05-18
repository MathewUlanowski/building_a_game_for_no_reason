from math import pi, sqrt
from numpy import arccos


class EntityModel:
    def __init__(self,location:tuple) -> None:
        self.Location = location
    
    def Distance(self,point:tuple):
        return sqrt((self.Location[0]-point[0])**2 + (self.Location[1]-point[1])**2)
    def AngleFromUp(self,point:tuple):
        x_axis_angle_dif = (arccos(abs(self.Location[0]-point[0])/self.Distance(point)))  * (180/pi)
        if point[1] - self.Location[1] <= 0 and point[0] - self.Location[0] >=1:
            return 90 - x_axis_angle_dif
        elif point[1] - self.Location[1] >= 0 and point[0] - self.Location[0] >=1:
            return 90 + x_axis_angle_dif
        elif point[1] - self.Location[1] >= 0 and point[0] - self.Location[0] <=1:
            return 270 - x_axis_angle_dif
        elif point[1] - self.Location[1] <= 0 and point[0] - self.Location[0] <=1:
            return 270 + x_axis_angle_dif