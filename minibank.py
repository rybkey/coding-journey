balance = 1000

transactions = []

def check_balance():
    print(f'Your balance is ${round(balance, 2)}')

def deposit():
    global balance

    print('How much do you want to deposit?')
    while True:
        try:
            user_input = float(input())
            if user_input <= 0:
                print('You can only deposit an amount higher than 0!')
            else:
                break
        except ValueError:
            print('You can only input a number!')

    balance += user_input
    print(f'You have added ${user_input} to your account')

    new_deposit = ['deposit', user_input]
    transactions.append(new_deposit)

def withdraw():
    global balance

    print('How much do you want to withdraw?')
    while True:
        try:
            user_input = float(input())
            if user_input <= 0:
                print('You can only withdraw an amount higher than 0!')
            else:
                if user_input > balance:
                    print('You don\'t have this much money on your account!')
                else:
                    break
        except ValueError:
            print('You can only input a number!')

    balance -= user_input
    print(f'You have withdrawn ${user_input} from your account')
    
    new_withdrawal = ['withdrawal', user_input]
    transactions.append(new_withdrawal)


def history():
    if len(transactions) > 0:
        for index, transaction in enumerate(transactions):
            print(f'{index + 1}. {transaction[0].capitalize()} - ${transaction[1]}')
    else:
        print('You don\'t have any transactions yet!')



while True:
    print('### BANK ###')
    print('1. Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. History')
    print('5. Exit')

    while True:
        user_input = input()
        if user_input not in ['1', '2', '3', '4', '5']:
            print('You can only choose 1, 2, 3, 4, 5!')
        else:
            break

    match user_input:
        case '1':
            check_balance()
        case '2':
            deposit()
        case '3':
            withdraw()
        case '4':
            history()
        case '5':
            exit()

    print()