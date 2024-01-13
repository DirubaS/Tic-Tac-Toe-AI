# settings.py

import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diruba's Tic Tac Toe")

CELL_SIZE = 200
MARGIN = 8

bg_image = pygame.image.load("bg.png")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

board = np.zeros((3, 3))

AI = 1
HUMAN = -1

AI_cir_image = pygame.image.load("AI_cir.png")
human_cross_image = pygame.image.load("human_cross.png")

game_font = pygame.font.SysFont("arial", 70)

white = pygame.Color("white")
blue = pygame.Color("#8114FF")
