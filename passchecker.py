
points = 0

passLength = False
passLower = False
passUpper = False
passLetter = False
passDigit = False
passChar = False

while True:
    print('Please type in your password:')
    password = input()

    if len(password) < 8:
        print("1")
    else:
        passLength = True
        points += 1
        
    if password.islower() == True:
        print("2")
    else:
        passLower = True
        points += 1

    if password.isupper() == True:
        print("3")
    else:
        passUpper = True
        points += 1

    if password.isdigit() == True:
        print("4")
    else:
        passLetter = True
        points += 1

    if any(character.isdigit() for character in password) == False:
        print("5")
    else:
        passDigit = True
        points += 1

    if any(character.isdigit() for character in password) == False and any(character.isalpha() for character in password) == False:
        print("6")
    else:
        passChar = True
        points += 1

    strength = 'None'

    if 0 < points <= 2:
        strength = 'Weak'
    if 2 < points <= 4:
        strength = 'Normal'
    if points == 5:
        strength = 'Strong'
    if points == 6:
        strength = 'Unbreakable'

    print('# PASSWORD ASSESSMENT')
    print()
    print(f'Strength: {strength}')
    print()
    print('Weaknesses:')
    if passLength == False:
        print('Your password is too short!')
    if passLower == False:
        print('Your password should contain at least one uppercase letter!')
    if passUpper == False:
        print('Your password should contain at least one lowercase letter')
    if passLetter == False:
        print('Your password cannot consist only of digits')
    if passDigit == False:
        print('Your password should contain at least one number')
    if passChar == False:
        print('Your password should contain a special character!')

    if points == 8:
        break

    print()