import json


class Configuration:
    def __init__(self):
        # load file
        f = open("./settings.json", "r")
        settings = json.loads(f.read())

        # grabs the json object and converts it to a touple that the game understands
        dim = settings["dimensions"]
        self.WindowDimensions:tuple = (dim[0],dim[1])
        # converts the list to a tuple the game understands
        bc = settings["background_color"]
        self.BackgroundColor:tuple = (bc[0],bc[1],bc[2])
        self.FrameRate:int = settings["frame_rate"]