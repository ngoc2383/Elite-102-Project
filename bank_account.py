import sqlite3

class BankAccount:
    def __init__(self, user_id = '000000', password = None):
        self.user_id = user_id
        self.password = password
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def get_pass(self):
        self.cursor.execute('SELECT password FROM accounts WHERE user_id = ?', (self.user_id,))
        password = self.cursor.fetchone()
        if password:
            return password[0]
        return None

    def acc_existed(self):
        self.cursor.execute('SELECT user_id FROM accounts')
        user_id = self.cursor.fetchall()

        if user_id:
            for i in range(len(user_id)):
                user_id[i] = ('').join(user_id[i])
            return user_id
        return None

    def create_table(self):
         # Create the accounts table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance REAL DEFAULT 0.0,
                password TEXT
            )
        ''')
        self.conn.commit()

    def create_account(self, user_id = '', password = ''):
        if user_id == '':
            user_id = self.user_id
        if password == '':
            password = self.password

        self.cursor.execute('INSERT OR IGNORE INTO accounts (user_id, balance, password) VALUES (?, ?, ?)', (user_id, 0.0, password))
        self.conn.commit()

    def get_balance(self):
        self.cursor.execute('SELECT balance FROM accounts WHERE user_id = ?', (self.user_id,))
        balance = self.cursor.fetchone()
        
        if balance:
            return balance[0]
        else:
            return 0.0
    
    def deposit(self, amount):
        self.cursor.execute(
            'UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (amount, self.user_id))
        self.conn.commit()


    def withdraw(self, amount):
        current_balance = self.get_balance()
        if amount <= current_balance:
            # Subtract from balance
            self.cursor.execute(
                'UPDATE accounts SET balance = balance - ? WHERE user_id = ?',
                (amount, self.user_id)
            )

            self.conn.commit()
        else:
            print("Not enough funds to withdraw.")

    def delete_acc(self, delete_id):
        self.cursor.execute('DELETE FROM accounts WHERE user_id = ?', (delete_id,))
        self.conn.commit()

    def delete_placeholder(self):
        self.cursor.execute('DELETE FROM accounts WHERE password IS NULL')
        self.conn.commit()

