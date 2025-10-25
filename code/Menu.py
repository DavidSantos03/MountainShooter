import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.const import WINDOW_WIDTH, COLOR_PRIMARY, MENU_OPTIONS, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0

        pygame.mixer_music.load('./assets/sounds/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.build_menu_text(60, "Mountain", COLOR_PRIMARY, (WINDOW_WIDTH / 1.1, 60))
            self.build_menu_text(60, "Shooter", COLOR_PRIMARY, (WINDOW_WIDTH / 1.1, 100))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.build_menu_text(25, MENU_OPTIONS[i], COLOR_YELLOW, (WINDOW_WIDTH / 1.1, (160 + (25 * i))))
                else:
                    self.build_menu_text(25, MENU_OPTIONS[i], COLOR_WHITE, (WINDOW_WIDTH / 1.1, (160 + (25 * i))))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < (len(MENU_OPTIONS) - 1):
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

    def build_menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
