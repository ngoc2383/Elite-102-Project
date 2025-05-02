import sqlite3

class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0
            )
        ''')
        self.conn.commit()

    def create_account(self):
        self.cursor.execute('INSERT OR IGNORE INTO accounts (user_id, balance) VALUES (?, ?)', (self.user_id, 0.0))
        self.conn.commit()
    
    
    # ============================================================================
    def create_pokemon_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Pokemon_info (
            Pokemon TEXT,
            PokemonType TEXT,
            PokeDexNum INTEGER
            )
        ''')
        self.conn.commit()

    def create_pokemon(self):
        self.cursor.execute('''
        INSERT INTO Pokemon_info (Pokemon, PokemonType, PokeDexNum)VALUES 
            ('Bulbasaur', 'Grass', 1),
            ('Charmander', 'Fire', 4),
            ('Squirtle', 'Normal', 7);
    ''')

