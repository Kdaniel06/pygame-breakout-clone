import pygame
from random import randrange 

## *  --- SETTINGS ---
WIDTH, HEIGHT = 1200, 600
FPS = 60

# * PADDLE SETTINGS
PADDLE_WIDTH = 250
PADDLE_HEIGHT = 20
PADDLE_SPEED = 15
PADDLE = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# * BALL SETTINGS
BALL_RADIUS = 15
BALL_SPEED = 5
BALL_RECT = int(BALL_RADIUS * 2 ** 0.5)
BALL = pygame.Rect(randrange(BALL_RECT, WIDTH - BALL_RECT), HEIGHT // 2, BALL_RECT, BALL_RECT)
DX, DY = 1, -1 # ? Redirection and collision of the ball

# * BLOCK SETTINGS
BLOCK_LIST = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
COLOR_LIST = [(randrange(30, 256), randrange(30, 256), randrange(30, 256)) for i in range(10) for j in range(4)]