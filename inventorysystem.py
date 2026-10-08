
inventory = [
    {'name': 'Flashlight', 'amount': 1}
]

def show_inventory():
    print()
    print('### INVENTORY ###')
    if len(inventory) > 0:
        for index, item in enumerate(inventory):
            print(f'{index + 1}. {item['name']}, Quantity: {item['amount']}')
    else:
        print('You have no items yet!')

def add_item():
    print('### ADDING AN ITEM ###')

    print('Write the name of the item:')
    name_input = input()
 
    while True:
        print('How many are we adding?')
        try:
            amount_input = int(input())
            if amount_input <= 0:
                print('You can\'t choose a number lower than 1')
            else:
                break
        except ValueError:
            print('You can only pass the number')

    found = False
    for item in inventory:       
        if item['name'].lower() == name_input.lower():
            item['amount'] += amount_input 
            found = True
    if not found:
        new_item = {
            'name': name_input,
            'amount': amount_input
        }
        inventory.append(new_item)

    print(f'You successfully added {amount_input} of {name_input}')

def remove_item():
    print('### REMOVE AN ITEM ###')
    if len(inventory) > 0:
        for index, item in enumerate(inventory):
            print(f'{index + 1}. {item['name']}, Quantity: {item['amount']}')        

        while True:
            print('What item do you want to remove (write the index)?')

    
            try:
                index_input = int(input()) - 1
                if 0 < index_input + 1 <= (len(inventory)):
                    break
                else:
                    print('There is no such index!')
            except ValueError:
                print('You can only pass the number')

        while True:
            print(f'How many do you want to remove?')
            try:
                amount_input = int(input())
                if amount_input <= 0:
                    print('You can\'t choose a number lower than 1')
                elif inventory[index_input]['amount'] - amount_input < 0:
                    print('You cannot delete this many because there are no this many')
                elif inventory[index_input]['amount'] - amount_input == 0:
                    print(f'There was nothing else of {inventory[index_input]['name']} so it was completely removed')
                    del inventory[index_input]
                    break
                else:
                    inventory[index_input]['amount'] -= amount_input
                    print(f'The amount of {inventory[index_input]['name']} has been reduced to {inventory[index_input]['amount']}')
                    break
            except ValueError:
                print('You can only pass the number')

    else:
        print('You have no items yet!')
    


while True:
    while True:
        print()
        print("### MENU ###")
        print('1. Show inventory')
        print('2. Add an item')
        print('3. Remove an item')

        user_input = input()
        if user_input not in ['1','2','3']:
            print('You can only choose between options 1, 2, 3')
        else:
            break

    match user_input:
        case '1': 
            show_inventory()
        case '2':
            add_item()
        case '3':
            remove_item()

