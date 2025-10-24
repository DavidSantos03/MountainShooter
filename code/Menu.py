import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_PRIMARY, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./assets/sounds/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.build_menu_text(60, "Mountain", COLOR_PRIMARY, (WINDOW_WIDTH / 1.1, 60))
            self.build_menu_text(60, "Shooter", COLOR_PRIMARY, (WINDOW_WIDTH / 1.1, 100))

            for i in range(len(MENU_OPTIONS)):
                self.build_menu_text(25, MENU_OPTIONS[i], COLOR_WHITE, (WINDOW_WIDTH / 1.1, (160 + (25 * i))))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
            pass

    def build_menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
