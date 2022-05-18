from math import sqrt


def Distance(posint1:tuple,point2:tuple):
        return sqrt((posint1[0]-point2[0])**2 + (posint1[1]-point2[1])**2)