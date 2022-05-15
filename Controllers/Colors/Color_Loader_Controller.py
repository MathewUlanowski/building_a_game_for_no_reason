from glob import glob
from Models.Colors.Color_Model import ColorPallete
from Models.Colors.Color_Schema_Model import ColorSchema


def Load_Pallete(path):
    return ColorPallete(path)

def Load_Schema(path):
    schema = ColorSchema()
    for fileName in glob(path+"/*.json"):
        key = fileName.rsplit("\\", 1)[1].replace(".json","")
        schema.addPalette(key,ColorPallete(fileName))
    return schema
