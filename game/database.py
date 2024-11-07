import os
import sqlite3

class Database:
    def __init__(self, db_path='data/game_data.sqlite'):
        self.db_path = db_path
        self.check_data_directory()
        self.check_database()

    def check_data_directory(self):
        """Verifica se a pasta 'data/' existe, se não, cria a pasta."""
        if not os.path.exists('data'):
            os.makedirs('data')

    def check_database(self):
        """Verifica se o banco de dados SQLite existe e se contém os schemas necessários."""
        if not os.path.exists(self.db_path):
            print("Banco de dados não encontrado. Criando um novo.")
            self.create_database()
        else:
            self.verify_schemas()

    def create_database(self):
        """Cria um novo banco de dados e os schemas necessários."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Criação da tabela de sessões
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY,
                name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Criação das tabelas para jogadores, submarinos e tesouros
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                session_id INTEGER,
                name TEXT,
                score INTEGER,
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS submarines (
                id INTEGER PRIMARY KEY,
                session_id INTEGER,
                player_id INTEGER,
                position_x INTEGER,
                position_y INTEGER,
                FOREIGN KEY (session_id) REFERENCES sessions (id),
                FOREIGN KEY (player_id) REFERENCES players (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS treasures (
                id INTEGER PRIMARY KEY,
                session_id INTEGER,
                position_x INTEGER,
                position_y INTEGER,
                FOREIGN KEY (session_id) REFERENCES sessions (id)
            )
        ''')
        
        conn.commit()
        conn.close()


    def verify_schemas(self):
        """Verifica se as tabelas necessárias existem no banco de dados."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Verifica se as tabelas existem
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = {table[0] for table in cursor.fetchall()}

        required_tables = {'players', 'submarines', 'treasures'}
        missing_tables = required_tables - tables

        if missing_tables:
            print(f"Tabelas ausentes: {missing_tables}. Criando as tabelas necessárias.")
            self.create_database()

        conn.close()

    def start_new_game(self, save_name, players):
        """Inicia um novo jogo e salva a sessão no banco de dados."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Cria uma nova sessão
        cursor.execute("INSERT INTO sessions (name) VALUES (?)", (save_name,))
        session_id = cursor.lastrowid  # Obtém o ID da nova sessão

        conn.commit()
        conn.close()

    def get_saved_games(self):
        """Consulta o banco de dados e retorna uma lista de jogos salvos."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sessions")  # Supondo que você tenha uma tabela de jogadores
        saved_games = cursor.fetchall()
        conn.close()
        return saved_games