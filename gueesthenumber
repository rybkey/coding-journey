import random

number = random.randint(1, 100)

print('Guess the number: ')

while True:
    while True:
        user_input = input()
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print('You have to type in a number! Try again!')
            

    if user_input == number:
        print('You have successfully guessed the number!')
        break
    elif number > user_input:
        print('Try a higher number!')
    elif number < user_input:
        print('Try a lower number!')

