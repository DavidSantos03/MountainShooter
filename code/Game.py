import pygame
from code.Menu import Menu
from code.const import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_HEIGHT, WINDOW_WIDTH))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                pass
            elif menu_return == MENU_OPTIONS[1]:
                pass
            elif menu_return == MENU_OPTIONS[2]:
                pass
            elif menu_return == MENU_OPTIONS[3]:
                pass
            elif menu_return == MENU_OPTIONS[4]:
                pygame.quit()  # Close window
                quit()  # End pygame

