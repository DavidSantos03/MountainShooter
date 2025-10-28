import pygame

# C
COLOR_PRIMARY = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLACK = (0, 0, 0)

# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 4,
    'Player2': 4,
    'Enemy1': 2,
    'Enemy2': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTIONS = ('NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P - COMPETITIVE',
                'SCORE',
                'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# W
WINDOW_HEIGHT = 576
WINDOW_WIDTH = 324
