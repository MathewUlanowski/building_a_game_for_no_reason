import json


class Configuration:
    def __init__(self, settings_path) -> None:
        # load file
        f = open(settings_path, "r")
        settings = json.loads(f.read())

        # grabs the json object and converts it to a touple that the game understands
        dim = settings["dimensions"]
        self.window_dimensions = (dim[0],dim[1])
        # converts the list to a tuple the game understands
        bc = settings["background_color"]
        self.background_color = (bc[0],bc[1],bc[2])