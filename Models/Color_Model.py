import json
from logging import warn


class ColorPallete:
    def __init__(self,jsonFilePath):
        f = open(jsonFilePath, "r")
        self.__filepath = jsonFilePath
        self.ColorList = {}
        jsonColors = json.loads(f.read())
        for k in jsonColors:
            color = jsonColors[k]
            self.ColorList[k] = (color[0],color[1],color[2])
    
    def GetColor(self, color):
        try:
            return (self.ColorList[color])
        except:
            warn(f"Error finding color '{color}' in {self.__filepath}")
            return (255,0,0)