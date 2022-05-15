from typing import List
import pygame


class EventController:
    def __init__(self):
        self.__ToggledInputs = []
        self.Run_Condition = True

    def Key_Event_Handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Run_Condition = False

            if event.type == pygame.KEYDOWN:
                self.AddToggle(event.key)
            if event.type == pygame.KEYUP:
                self.RemoveToggle(event.key)

    def AddToggle(self,event):
        try:
            self.__ToggledInputs.append(event)
            print(f"Added: {event}")
        except:
            print("error adding event:\n".upper() + str(event))
    def RemoveToggle(self,event):
        try:
            self.__ToggledInputs.remove(event)
            print(f"Removed: {event}")
        except:
            print("error removing event:\n".upper() + str(event))
    def getToggles(self):
        return self.__ToggledInputs

    def IsToggled(self,key:int):
        return True if key in self.getToggles() else False
    def QuitGame(self):
        self.Run_Condition = False