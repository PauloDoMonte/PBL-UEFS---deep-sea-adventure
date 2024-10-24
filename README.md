# Submarine Game

Um jogo de aventura em que os jogadores exploram um mapa subaquático em busca de tesouros, enquanto gerenciam o consumo de oxigênio e evitam bombas. O jogo é desenvolvido em Python utilizando a biblioteca Pygame.

## Índice

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

## Visão Geral

O Submarine Game é um jogo para 4 jogadores onde cada um controla um mergulhador que deve coletar tesouros em um mapa subaquático. Os jogadores devem gerenciar o consumo de oxigênio, que é afetado pelo peso dos tesouros coletados e pela profundidade em que estão mergulhando. O jogo também inclui bombas que podem ser encontradas no mapa, e os jogadores devem evitá-las para não perder a partida.

## Instalação

Para executar o jogo, você precisará ter o Python 3 e a biblioteca Pygame instalados. Siga os passos abaixo para configurar o ambiente:

1. Clone o repositório:
	git clone <URL_DO_REPOSITORIO>
	cd submarine_game

2. Crie um ambiente virtual (opcional, mas recomendado):
	python -m venv venv
	source venv/bin/activate

3. Instale as dependências
	pip3 install -r requirements.txt

## Uso

Para iniciar o jogo, execute o seguinte comando:

python3 main.py

O jogo abrirá uma janela onde você poderá acessar o menu inicial, configurar as opções e iniciar a partida. Siga as instruções na tela para jogar, incluindo a seleção de dificuldade e a movimentação dos jogadores no mapa subaquático.

## Estrutura do projeto

A estrutura do projeto é organizada da seguinte forma:

│
├── main.py                # Ponto de entrada do jogo
├── game/                  # Módulo principal do jogo
│   ├── __init__.py
│   ├── game.py            # Lógica do jogo e gerenciamento de estados
│   ├── player.py          # Classe para gerenciar os jogadores
│   ├── submarine.py        # Classe para o submarino
│   ├── treasure.py        # Classe para os tesouros
│   ├── bomb.py            # Classe para as bombas
│   └── map.py             # Classe para o mapa do jogo
│
├── assets/                # Recursos do jogo (imagens, sons, etc.)
│   ├── images/
│   └── sounds/
│
└── utils/                 # Utilitários e constantes
    ├── __init__.py
    └── constants.py       # Constantes usadas no jogo

## Como Contribuir
Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga estas etapas:
1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nome-da-sua-feature`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-sua-feature`).
5. Abra um Pull Request.
