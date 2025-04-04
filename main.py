def hello_user():
    print('Hello, how might I help you today?')
    print('Plese choose from the opions below to continue')
    print('1. _________________\n2. _______________________\n3. __________________\n4. ________________________')

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
