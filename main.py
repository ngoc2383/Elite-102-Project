from bank_account import BankAccount

user_id = input("Enter your user ID: ")
account = BankAccount(user_id)
account.create_account()
account.create_pokemon_table()
account.create_pokemon()

def hello_user():
    print('Hello, how might I help you today?')
    print('Plese choose from the opions below to continue')
    print('1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit')

def user_choice():
    choice = None
    while choice is None:
        try:
            choice = int(input('Your choice: '))
        except TypeError:
            choice = None
        if choice > 4 or choice < 1:
            choice = None
    return choice

def main():
    pass

