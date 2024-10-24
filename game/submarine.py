import pygame
from utils.constants import PLAYER1_COLOR, COLS, CELL_SIZE, SCREEN_WIDTH

class Submarine:
    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, 10)  # Posição inicial do submarino

    def draw(self, screen):
        # Desenhar o submarino na tela
        ship_width = COLS * CELL_SIZE // 2  # Metade da largura do tabuleiro
        ship_x = (SCREEN_WIDTH - ship_width) // 2  # Centralizado horizontalmente
        pygame.draw.ellipse(screen, PLAYER1_COLOR, (ship_x, self.position[1], ship_width, 40))
