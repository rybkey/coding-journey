import random

while True:
    print('Provide your first name:')
    name = input().lower()
    if name.isalpha():
        if len(name) < 2:
            print('Your name must contain at least 2 characters!')
        else:
            break
    else:
        print('Your name cannot contain other symbols, spaces, or numbers!')

while True:
    print('Provide your last name:')
    last_name = input().lower()
    if last_name.isalpha():
        if len(last_name) < 2:
            print('Your last name must contain at least 2 characters!')
        else:
            break
    else:
        print('Your last name cannot contain other symbols, spaces, or numbers!')

while True:
    try:
        print('Provide the year you were born in:')
        year = int(input())
        if 1900 > year:
            print('You cannot be that old!')
        elif year > 2026:
            print('You are not even born yet!')
        else:
            year = str(year)
            break
    except ValueError:
        print('You can only input a number!')

print('Username options:')
print(name + last_name)
print(name + year)
print(name[:2] + last_name + year[-2:])
print(name + last_name[:3] + '_' + year)
print(name[:2] + '_' + last_name[:3] + year[-2:])

patterns_name = [name, name[:2]]
patterns_last_name = [last_name, last_name[:3]]
patterns_year = [year, year[-2:]]
spaces = ['', '', '_']
used_names = []

print('Random usernames:')
for i in range(5):
    while True:
        new_name = random.choice(patterns_name) + random.choice(spaces) + random.choice(patterns_last_name) + random.choice(spaces) + random.choice(patterns_year)
        if new_name not in used_names:
            used_names.append(new_name)
            print(used_names[i])
            break