import random

words = ['apple', 'paper', 'floor', 'happy']
word = random.choice(words)

starter = list(word)
letters = starter.copy()

while True:
    random.shuffle(letters)
    if letters != starter:
        break

attempts = 3

while True:
    print('The shuffled word is: ' + ''.join(letters))
    print('Try to guess it!')
    while True:
        guess = input().lower()
        if guess.isalpha():
            break
        else:
            print('Your guess cannot contain numbers, spaces, or other symbols!')

    if guess == word:
        print('You have successfully guessed the word!')
        print(f'The word was: {word}')
        break
    else:
        print('No, unfortunately it\'s not the word!')
        attempts -= 1

    if attempts <= 0:
        print('You are out of attempts! You lost!')
        print(f'The word was: {word}')
        break

    print(f'Remaning attempts: {attempts}')