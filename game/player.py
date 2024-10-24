import pygame
from utils.constants import PLAYER1_COLOR

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = (0, 0)  # Posição inicial
        self.treasures = []
        self.oxygen_tanks = 500  # Exemplo de quantidade inicial

    def draw(self, screen):
        # Desenhar o jogador na tela
        pygame.draw.circle(screen, PLAYER1_COLOR, self.position, 10)
