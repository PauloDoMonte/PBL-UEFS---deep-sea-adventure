import pygame
import sys, random
from .player import Player
from .submarine import Submarine
from .map import GameMap
from .database import Database
from utils.constants import *

class Game:
    def __init__(self):
        self.database = Database()
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
                self.input_save_name()()  # Chama a função do jogo
            if self.draw_button("Carregar Jogo", 300, 300, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                self.load_game_menu()  # Chama o menu de carregar jogo
            if self.draw_button("Configurações", 300, 400, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                self.settings()
            if self.draw_button("Sair", 300, 500, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
    
    def load_game_menu(self):
        load_running = True
        while load_running:
            self.screen.fill(DARK_BG)
            title_text = pygame.font.Font(None, 50).render("Carregar Jogo", True, BORDER_COLOR)
            self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

            saved_games = self.database.get_saved_games()

            if saved_games:
                for i, game in enumerate(saved_games):
                    game_text = pygame.font.Font(None, 30).render(f"Jogo {i + 1}: {game[1]}", True, BORDER_COLOR)
                    self.screen.blit(game_text, (SCREEN_WIDTH // 2 - game_text.get_width() // 2, 150 + i * 40))
            else:
                no_games_text = pygame.font.Font(None, 30).render("Nenhum jogo salvo.", True, BORDER_COLOR)
                self.screen.blit(no_games_text, (SCREEN_WIDTH // 2 - no_games_text.get_width() // 2, 150))

            if self.draw_button("Voltar ao Menu", 300, 400, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                return  # Retorna ao menu principal

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def input_save_name(self):
        """Exibe um menu para o usuário digitar o nome do novo save."""
        input_running = True
        save_name = ""
        while input_running:
            self.screen.fill(DARK_BG)
            title_text = pygame.font.Font(None, 50).render("Digite o nome do save:", True, BORDER_COLOR)
            self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

            # Renderiza o texto do nome do save
            input_text = pygame.font.Font(None, 40).render(save_name, True, BORDER_COLOR)
            self.screen.blit(input_text, (SCREEN_WIDTH // 2 - input_text.get_width() // 2, 150))

            if self.draw_button("Confirmar", 300, 250, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                if save_name:  # Verifica se o nome não está vazio
                    self.database.start_new_game(save_name, self.players)  # Inicia o novo jogo com o nome do save
                    self.game_loop()  # Chama a função do jogo
                else:
                    # Mensagem de erro se o nome estiver vazio
                    error_text = pygame.font.Font(None, 30).render("Por favor, insira um nome válido.", True, (255, 0, 0))
                    self.screen.blit(error_text, (SCREEN_WIDTH // 2 - error_text.get_width() // 2, 350))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        save_name = save_name[:-1]  # Remove o último caractere
                    elif event.key == pygame.K_RETURN:
                        if save_name:  # Verifica se o nome não está vazio
                            self.database.start_new_game(save_name, self.players)  # Inicia o novo jogo com o nome do save
                            self.game_loop()  # Chama a função do jogo
                    else:
                        save_name += event.unicode  # Adiciona o caractere digitado

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