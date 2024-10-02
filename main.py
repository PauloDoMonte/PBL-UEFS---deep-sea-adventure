import pygame
import sys
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores no estilo "Dracula"
DARK_BG = (40, 42, 54)
DARK_CELL = (68, 71, 90)
BORDER_COLOR = (189, 147, 249)
PLAYER1_COLOR = (255, 85, 85)
PLAYER2_COLOR = (139, 233, 253)
BUTTON_COLOR = (98, 114, 164)
BUTTON_HOVER_COLOR = (255, 121, 198)
BUTTON_SELECTED_COLOR = (100, 255, 100)  # Cor para o botão selecionado
TREASURE_COLOR = (255, 223, 0)  # Cor para representar o tesouro (ouro)

# Dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonte para os textos
font = pygame.font.Font(None, 50)

# Dimensões do tabuleiro
ROWS = 15
COLS = 15
CELL_SIZE = 18  # Tamanho de cada célula

# Quantidade de tesouros
NUM_TREASURES = 15

# Dificuldades disponíveis
DIFFICULTIES = ["Fácil", "Moderado", "Difícil", "Insano"]
selected_difficulty = None  # Dificuldade selecionada

# Função para desenhar botões
def draw_button(text, x, y, w, h, color, hover_color, selected=False):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Se o mouse estiver sobre o botão, muda a cor
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1:
            return True
    else:
        if selected:
            pygame.draw.rect(screen, BUTTON_SELECTED_COLOR, (x, y, w, h))  # Cor do botão selecionado
        else:
            pygame.draw.rect(screen, color, (x, y, w, h))

    # Texto do botão
    text_surf = font.render(text, True, BORDER_COLOR)
    text_rect = text_surf.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surf, text_rect)
    return False

# Função para desenhar as setas de controle
def draw_control_arrows():
    arrow_size = 50  # Tamanho das setas
    arrow_spacing = 40  # Espaçamento entre as setas
    vertical_spacing = 40  # Espaçamento vertical (acima e abaixo)
    horizontal_spacing = 40  # Espaçamento horizontal (direita)
    bottom_arrow_spacing = 20  # Espaçamento abaixo do mapa
    arrow_offset_x = 10  # Posição x no canto inferior esquerdo
    arrow_offset_y = 500  # Posição y ajustada abaixo do mapa

    # Setas para cima, baixo, esquerda e direita
    up_arrow = pygame.Rect(
        horizontal_spacing + arrow_offset_x + arrow_size // 2,
        arrow_offset_y - arrow_size,
        arrow_size,
        arrow_size
    )
    
    down_arrow = pygame.Rect(
        horizontal_spacing + arrow_offset_x + arrow_size // 2,
        arrow_offset_y + vertical_spacing,
        arrow_size,
        arrow_size
    )
    
    left_arrow = pygame.Rect(
        arrow_offset_x,
        bottom_arrow_spacing + arrow_offset_y - arrow_size // 2,
        arrow_size,
        arrow_size
    )
    
    right_arrow = pygame.Rect(
        horizontal_spacing + arrow_offset_x + arrow_size + arrow_spacing,
        bottom_arrow_spacing + arrow_offset_y - arrow_size // 2,
        arrow_size,
        arrow_size
    )

    # Desenha as setas
    pygame.draw.polygon(screen, BORDER_COLOR, [(up_arrow.centerx, up_arrow.top), 
                                                  (up_arrow.left, up_arrow.bottom), 
                                                  (up_arrow.right, up_arrow.bottom)])  # seta para cima

    pygame.draw.polygon(screen, BORDER_COLOR, [(down_arrow.centerx, down_arrow.bottom), 
                                                  (down_arrow.left, down_arrow.top), 
                                                  (down_arrow.right, down_arrow.top)])  # seta para baixo

    pygame.draw.polygon(screen, BORDER_COLOR, [(left_arrow.left, left_arrow.centery), 
                                                  (left_arrow.right, left_arrow.top), 
                                                  (left_arrow.right, left_arrow.bottom)])  # seta para esquerda

    pygame.draw.polygon(screen, BORDER_COLOR, [(right_arrow.right, right_arrow.centery), 
                                                  (right_arrow.left, right_arrow.top), 
                                                  (right_arrow.left, right_arrow.bottom)])  # seta para direita


    # Verifica se o usuário clica em alguma seta
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if up_arrow.collidepoint(mouse):
        if click[0] == 1:
            print("Clicou na seta para cima")  # Aqui você pode adicionar a lógica para mover o submarino para cima
    elif down_arrow.collidepoint(mouse):
        if click[0] == 1:
            print("Clicou na seta para baixo")  # Lógica para mover para baixo
    elif left_arrow.collidepoint(mouse):
        if click[0] == 1:
            print("Clicou na seta para esquerda")  # Lógica para mover para a esquerda
    elif right_arrow.collidepoint(mouse):
        if click[0] == 1:
            print("Clicou na seta para direita")  # Lógica para mover para a direita

# Função para desenhar o painel de controle
def draw_control_panel(treasures):
    # Desenha a área do painel de controle
    pygame.draw.rect(screen, DARK_CELL, (0, 0, 300, SCREEN_HEIGHT))
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, 300, SCREEN_HEIGHT), 2)

    # Desenha seção de oxigênio
    oxygen_text = font.render("Oxigênio: 100%", True, PLAYER1_COLOR)
    screen.blit(oxygen_text, (10, 10))

    # Desenha seção da condição do submarino
    condition_text = font.render("Condição: Normal", True, PLAYER1_COLOR)
    screen.blit(condition_text, (10, 60))

    # Mapa (simples representação)
    map_text = font.render("Mapa", True, BORDER_COLOR)
    screen.blit(map_text, (10, 120))

    # Desenha o grid do mapa
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(10 + col * CELL_SIZE, 160 + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, PLAYER2_COLOR, rect, 1)  # Desenha borda da célula
            if (col, row) in treasures:
                pygame.draw.circle(screen, TREASURE_COLOR, rect.center, CELL_SIZE // 4)

    # Desenha as setas de controle
    draw_control_arrows()

# Função para desenhar o "submarino" (pequena elipse)
def draw_ship():
    ship_width = COLS * CELL_SIZE // 2  # Metade da largura do tabuleiro
    ship_x = (SCREEN_WIDTH - ship_width) // 2  # Centralizado horizontalmente
    ship_y = 10  # Posição no topo
    pygame.draw.ellipse(screen, PLAYER1_COLOR, (ship_x, ship_y, ship_width, 40))

# Função para criar a matriz do tabuleiro
def create_board():
    board = []
    for row in range(ROWS):
        # Cria uma linha de zeros
        board.append([0] * COLS)
    return board

# Função para gerar tesouros aleatórios no tabuleiro
def generate_treasures():
    treasures = []
    while len(treasures) < NUM_TREASURES:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        if (x, y) not in treasures:  # Verifica se o tesouro já foi gerado
            treasures.append((x, y))
    return treasures

# Função para o menu inicial
def menu():
    menu_running = True
    while menu_running:
        screen.fill(DARK_BG)

        # Título do menu
        title_text = font.render("Menu Inicial", True, BORDER_COLOR)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

        # Botões
        if draw_button("Iniciar", 300, 200, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
            game()  # Chama a função do jogo
        if draw_button("Configurações", 300, 300, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
            settings()
        if draw_button("Sair", 300, 400, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
            pygame.quit()
            sys.exit()

        # Eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Função para o jogo
def game():
    # Cria a matriz do tabuleiro
    board = create_board()
    treasures = generate_treasures()  # Gera tesouros aleatórios
    game_running = True

    while game_running:
        screen.fill(DARK_BG)

        # Desenha o "submarino"
        draw_ship()

        # Desenha o painel de controle com tesouros
        draw_control_panel(treasures)

        # Eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Função para as configurações
def settings():
    global selected_difficulty  # Permite modificar a variável fora da função
    settings_running = True
    while settings_running:
        screen.fill(DARK_BG)

        # Exibe uma mensagem indicando as configurações
        settings_text = font.render("Configurações", True, BORDER_COLOR)
        screen.blit(settings_text, (SCREEN_WIDTH // 2 - settings_text.get_width() // 2, 50))

        # Botões para seleção de dificuldade
        for i, difficulty in enumerate(DIFFICULTIES):
            y_position = 150 + (i * 70)  # Espaçamento vertical entre os botões
            if draw_button(difficulty, 300, y_position, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR, 
                           selected=(selected_difficulty == difficulty)):
                selected_difficulty = difficulty  # Atualiza a dificuldade selecionada

        # Botão para voltar ao menu
        if draw_button("Voltar ao Menu", 550, 500, 200, 60, BUTTON_COLOR, BUTTON_HOVER_COLOR):
            return  # Retorna ao menu

        # Eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Função principal
def main():
    menu()

# Executa o jogo
if __name__ == "__main__":
    main()
