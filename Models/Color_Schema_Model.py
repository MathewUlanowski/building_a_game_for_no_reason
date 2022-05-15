from Models.Color_Model import ColorPallete


class ColorSchema:
    def __init__(self):
        self.__palettes = {}
    
    def addPalette(self,paletteName, palette:ColorPallete):
        self.__palettes[paletteName] = palette
    def GetPalette(self,paletteName):
        return self.__palettes[paletteName]