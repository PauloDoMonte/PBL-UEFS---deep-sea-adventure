import pygame
import sys
import random
from .player import Player
from .submarine import Submarine
from .map import GameMap
from utils.constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.players = [Player(i) for i in range(4)]
        self.submarine = Submarine()
        self.game_map = GameMap()

    def run(self):
        self.menu()

    def menu(self):
        menu_running = True
        while menu_running:
            self.screen.fill(DARK_BG)
            title_text = pygame.font.Font(None, 50).render("Menu Inicial", True, BORDER_COLOR)
            self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

            if self.draw_button("Iniciar", 300, 200, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                self.game_loop()  # Chama a função do jogo
            if self.draw_button("Configurações", 300, 300, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                self.settings()
            if self.draw_button("Sair", 300, 400, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def game_loop(self):
        treasures = self.generate_treasures()  # Gera tesouros aleatórios
        game_running = True

        while game_running:
            self.screen.fill(DARK_BG)
            self.submarine.draw(self.screen)
            self.game_map.draw(self.screen, treasures)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def settings(self):
        settings_running = True
        while settings_running:
            self.screen.fill(DARK_BG)
            settings_text = pygame.font.Font(None, 50).render("Configurações", True, BORDER_COLOR)
            self.screen.blit(settings_text, (SCREEN_WIDTH // 2 - settings_text.get_width() // 2, 50))

            # Aqui você pode adicionar lógica para selecionar a dificuldade

            if self.draw_button("Voltar ao Menu", 550, 500, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                return  # Retorna ao menu

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def draw_button(self, text, x, y, w, h, color, hover_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen, hover_color, (x, y, w, h))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, color, (x, y, w, h))

        text_surf = pygame.font.Font(None, 50).render(text, True, BORDER_COLOR)
        text_rect = text_surf.get_rect(center=(x + w / 2, y + h / 2))
        self.screen.blit(text_surf, text_rect)
        return False

    def generate_treasures(self):
        treasures = []
        while len(treasures) < NUM_TREASURES:
            x = random.randint(0, COLS - 1)
            y = random.randint(0, ROWS - 1)
            if (x, y) not in treasures:  # Verifica se o tesouro já foi gerado
                treasures.append((x, y))
        return treasures