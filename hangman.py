import random

words = ['apple', 'banana', 'tomato', 'orange', 'melon']
guessed_letters = []
word_letters = []
ui_letters = []

word = random.choice(words)

for letter in word:
    word_letters.append(letter)
    ui_letters.append('_')

wrong = 0

while True:
    while True:
        user_input = input()

        if len(user_input) > 1:
            print('You may only check one letter at a time!')
        elif len(user_input) < 1:
            print('You have to check for at least one letter!')
        elif not user_input.isalpha():
            print('You have to input a LETTER!')
        elif user_input in guessed_letters:
            print('You already tried to guess this letter!')
        else:
            break

    search = 0

    for index, letter in enumerate(word_letters):
        if letter == user_input:
            search += 1
            ui_letters[index] = user_input

    guessed_letters.append(user_input)

    if search == 0:
        print(f'Unfortunately, there is no letter "{user_input}" in the word')
        wrong += 1
    else:
        print(f'You were right. The letter "{user_input}" appeared {search} times!')


    print('Word: ', end='')
    for index, letter in enumerate(ui_letters):
        if len(ui_letters) - 1 == index:
            print(ui_letters[index])
        else:
            print(ui_letters[index], end=', ')
    print(f'Wrong guesses: {wrong}/6')

    print()

    if wrong >= 6:
        print('You are out of guesses. You lost!')
        print(f'The word was {word}')
        break 
    if '_' not in ui_letters:
        print('Congratulations! You guessed the word!')
        print(f'The word was {word}')
        break