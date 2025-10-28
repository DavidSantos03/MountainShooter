import pygame

from code.Level import Level
from code.Menu import Menu
from code.Const import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_HEIGHT, WINDOW_WIDTH))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTIONS[3]:
                pass
            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()  # Close window
                quit()  # End pygame
