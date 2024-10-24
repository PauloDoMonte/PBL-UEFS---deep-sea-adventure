import pygame
from utils.constants import PLAYER2_COLOR, TREASURE_COLOR, CELL_SIZE, ROWS, COLS

class GameMap:
    def __init__(self):
        self.cells = [[0 for _ in range(COLS)] for _ in range(ROWS)]  # Matriz 15x15

    def draw(self, screen, treasures):
        # Desenha o grid do mapa
        for row in range(ROWS):
            for col in range(COLS):
                rect = pygame.Rect(10 + col * CELL_SIZE, 160 + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, PLAYER2_COLOR, rect, 1)  # Desenha borda da célula
                if (col, row) in treasures:
                    pygame.draw.circle(screen, TREASURE_COLOR, rect.center, CELL_SIZE // 4)
