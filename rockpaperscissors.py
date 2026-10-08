import random 

choices = ['rock', 'paper', 'scissors']
player_choice = None
computer_choice = None
player_points = 0
computer_points = 0

while player_points != 3 and computer_points != 3:
    
    while True:
        print('Choose your move:')
        print('rock, paper, scissors')
        player_choice = input().lower()
        if player_choice in choices:
            break
        else:
            print('There is no such move! Please try again!')

    computer_choice = random.choice(choices)

    if computer_choice == player_choice:
        print(f'We have a draw, you both chose {player_choice}')
    elif (computer_choice == 'paper' and player_choice == 'rock') or (computer_choice == 'rock' and player_choice == 'scissors') or (computer_choice == 'scissors' and player_choice == 'paper'):
        print(f'You chose {player_choice} but the computer chose {computer_choice}')
        print('You lost!')
        computer_points += 1
    else:
        print(f'You chose {player_choice} and the computer chose {computer_choice}')
        print('You won!')
        player_points += 1

    print(f'Score: You - {player_points}, Computer - {computer_points}')
    print()

if computer_points == 3:
    print('And now you\'ve lost for good.')
else:
    print('Congratulations, you finally won')
