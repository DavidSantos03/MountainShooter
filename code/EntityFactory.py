import random
from unittest import case

from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH + 252, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (0, 84))
            case 'Player2':
                return Player('Player2', (0, 100))
            case 'Enemy1':
                return Enemy('Enemy1', (WINDOW_WIDTH + 200, random.randint(0, WINDOW_HEIGHT)))
            case 'Enemy2':
                return Enemy('Enemy2', (WINDOW_WIDTH + 200, random.randint(0, WINDOW_HEIGHT)))
        return None

