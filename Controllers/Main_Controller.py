import pygame
from Models.Config import Configuration
from Models.Screen_Model import Screen


def GameLoop(config: Configuration):
    pygame.init()
    main_surface = Screen(config.window_dimensions, config.background_color, "My Boring Game")
    run_condition = True
    while run_condition:
        main_surface.refresh()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_condition = False
        main_surface.Update()
    pygame.quit()
    print("thank you for playing.")