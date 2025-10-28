import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_PRIMARY, WINDOW_WIDTH, COLOR_WHITE, WINDOW_HEIGHT, MENU_OPTIONS
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = 20000  # 20 seconds
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if self.game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

    def run(self):
        pygame.mixer_music.load(f'./assets/sounds/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Printed Text
            self.build_level_text(20, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, WINDOW_HEIGHT - 572))
            self.build_level_text(20, f'Fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WINDOW_HEIGHT - 555))
            self.build_level_text(20, f'Enemies: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 270))
            pygame.display.flip()

    def build_level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)#.convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
