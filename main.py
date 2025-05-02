from bank_account import BankAccount
from random import randint

def create_new_acc():
    print('** CREATE ACCOUNT **')
    input('Your name: ') # just random questions
    input('Your email: ')
    password = input('Your password: ')
    
    account = BankAccount()
    account.create_account()

    existed_id = account.acc_existed()
    user_id = str(randint(100000, 999999))
    
    if existed_id:
        for id in existed_id:
            if user_id == id:
                user_id = str(randint(100000, 999999))
    print(f'Your ID is: {user_id}')
    account.delete_placeholder()
    return user_id, password


def print_balance():
    print(f'Your balance: {account.get_balance()}')

def get_user_id():
    user_id = None
    while user_id is None:
        user_id = input("User ID (enter 0 if dont have an account): ")
        if user_id == '0':
            return 'new_acc'
        elif user_id.isdigit() == False:
            print('Your ID must not contain any letter\n')
            user_id = None
        elif len(user_id) != 6:
            print('Your ID must only be 6 digits long\n')
            user_id = None
    return user_id

while True:
    user_id = get_user_id()
    if user_id == 'new_acc': # acc created before log in
        user_id, password = create_new_acc()
        account = BankAccount(user_id, password)
        account.create_account()
        account.delete_placeholder()
    else:
        account = BankAccount(user_id)
        account.create_account()



    password = input('Password: ')
    if password == account.get_pass():
        break
    else:
        if account.get_pass() == None:
            account.delete_acc(user_id)
        print('Password doesnt match\nOr account not found\n')
        account.delete_placeholder()


def menu():
    print('=============================')
    print('1. Check Balance\n2. Deposit Funds\n3. Withdraw Funds\n4. Create new account\n5. Delete an account\n6. Exit')
    print('=============================')
def user_choice():
    choice = None
    while choice is None:
        try:
            choice = int(input('Your choice: '))
            if choice > 6 or choice < 1:
                print('Choice must be from 1 to 6\n')
                choice = None
        except ValueError:
            print('Choice must be a number!\n')
            choice = None
    return choice

def main():
    print('Hello, how might I help you today?')
    print('Plese choose from the opions below to continue')
    while True:
        menu()
        choice = user_choice()
        if choice == 1:
            print_balance()
        elif choice == 2:
            deposit_amount = int(input("How much do you wanna deposit: "))
            account.deposit(deposit_amount)
            print_balance()
        elif choice == 3:
            withdraw_amount = int(input("How much do you wanna withdraw: "))
            account.withdraw(withdraw_amount)
            print_balance()
        elif choice == 4:
            user_id, password = create_new_acc()
            account.create_account(user_id, password)
            print("Account created")
            print("Choose '7' to exit and run program again to log in\n")
        elif choice == 5:
            print('** DELETE ACCOUNT **')
            delete_id = input('ID to delete: ')
            
            if delete_id in account.acc_existed():
                account.delete_acc(delete_id)
                print('Deleted\n')
            else:
                print("Account doesnt exist")
            account.delete_placeholder()
        else:
            print('Thank you for using :)')
            account.delete_placeholder()
            break

main()

