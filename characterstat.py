
character_list = []

# If character exists, find under which index in characters_list he is
def name_collect():

    print('Write character\'s name:')
    while True:
        user_input = input()
        if user_input.isalpha() == False:
            print('You can only use letters!')
        else:
            break

    # If character is found it returns its index in character_list
    for index, character in enumerate(character_list):
        if user_input == character['name']:
            return index
        else:
            return None

def amount_collect():
    print('What amount should be used?')

    while True:
        while True:
            try: 
                user_input = int(input())
                break
            except ValueError:
                print('The amount can only be a number!')
        if user_input < 0:
            print('The amount cannot be lower than 0!')
        else:
            break

    return user_input

def create_character(health=100, attack=10):

    print('Write character\'s name:')

    while True:
        while True:
            user_input = input()
            if user_input.isalpha() == False:
                print('You can only use letters!')
            else:
                break

        doesExist = False
        for character in character_list:
            if user_input == character['name']:
                print(f'{character['name']} already exists! Try another name!')
            else:
                doesExist = True

        if doesExist == False:
            break

    print(f'Character {user_input} has been created')

    new_character = {'name': user_input, 'health': health, 'attack': attack}
    character_list.append(new_character)

def get_stats(index):

    if index is not None:

        print('### CHARACTER STATS ###')
        print(f'Name: {character_list[index]['name']}')
        print(f'Health: {character_list[index]['health']}')
        print(f'Attack: {character_list[index]['attack']}')
 
    else:
        print('This character does\'t exist!')

def take_damage(index, damage):

    if index is not None:

        if character_list[index]['health'] > damage:
            character_list[index]['health'] -= damage
            print(f'{character_list[index]['name']} received {damage} damage. {character_list[index]['name']}\'s current health is {character_list[index]['health']} HP')
        elif 0 < character_list[index]['health'] <= damage:
            print(f'{character_list[index]['name']} is unfortunately now down!')
            character_list[index]['health'] = 0
        else:
            print(f'{character_list[index]['name']} can\'t take any more damage because they are down')
  
    else:
        print('This character does\'t exist!')



def heal(index, amount, max_health=100):
   
    if index is not None:

        character_list[index]['health'] += amount
        if character_list[index]['health'] > max_health:
            character_list[index]['health'] = max_health
        print(f'{character_list[index]['name']} now has {character_list[index]['health']} HP!')
    
    else:
        print('This character does\'t exist!')


def display():
    if len(character_list) > 0:
        for character in character_list:
            print(f'Name: {character['name']}, Health: {character['health']}, Damage: {character['attack']}')
    else:
        print('You don\'t have any characters yet!')


while True:
    print('### MENU ###')
    print('1. Create character')
    print('2. Get character stats')
    print('3. Take damage')
    print('4. Heal character')
    print('5. Display characters')

    while True:
        user_input = input()
        if user_input not in ['1', '2', '3', '4', '5']:
            print('You can only choose between 1, 2, 3, 4, 5!')
        else:
            break

    match user_input:
        case '1':
            create_character()
        case '2':
            get_stats(name_collect())
        case '3':
            take_damage(name_collect(), amount_collect())
        case '4':
            heal(name_collect(), amount_collect())
        case '5':
            display()