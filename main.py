from Controllers.Main_Controller import GameLoop
from Models.Config import Configuration

config = Configuration("./settings.json")

def main():
    GameLoop(config)

if __name__ == "__main__":
    main()