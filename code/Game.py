import pygame
from code.Menu import Menu
from code.const import WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_HEIGHT, WINDOW_WIDTH))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

