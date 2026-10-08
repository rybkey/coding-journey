
tasks = []

with open ('tasks.txt', 'r') as file:
    for line in file.readlines():
        tasks.append(line.strip())


def view_tasks():
    print()
    print('### TASK LIST ###')

    if not tasks:
        print('You dont have any tasks yet!')
        return

    for task in tasks:
        print(f'- {task}')

def add_task():
    print()
    print('What is the name of the task?')

    while True:
        user_input = input().strip()
        if len(user_input) > 0:
            break
        else:
            print('You can\'t have an empty task!')
        
    tasks.append(user_input)
    print(f'You have succesfully added "{user_input}" as a new task')

def remove_task():
    print()
    print('### TASK DELETION ###')

    if not tasks:
        print('You dont have any tasks yet!')
        return

    for index, task in enumerate(tasks):
        print(f'{index + 1}. {task}')
    
    print('Provide the index of the task you would like to remove:')

    while True:
        try:
            user_input = int(input())
            if user_input <= 0:
                print('Come on, indexes cannot be zero or lower (in the list you see)')
            elif user_input > len(tasks):
                print('You don\'t have that many tasks. Choose the available ones')
            else:
                break
        except ValueError:
            print('You can only provide an index!')

    print(f'Task {tasks[user_input - 1]} has been successfully deleted from the list!')
    tasks.pop(user_input - 1)

def save_changes():
    print()
    with open('tasks.txt', 'w') as file:
        text = '\n'.join(tasks)
        file.write(text)
    print('Changes have been saved.')

while True:

    print()
    print('### TO DO APP ###')
    print('1. View tasks')
    print('2. Add task')
    print('3. Remove task')
    print('4. Save changes')
    print('5. Exit')

    while True:
        user_input = input()
        if user_input in ['1','2','3','4','5']:
            break
        else:
            print('You can only input 1, 2, 3, 4 or 5')

    match user_input:
        case '1':
            view_tasks()
        case '2':
            add_task()
        case '3':
            remove_task()
        case '4':
            save_changes()
        case '5':
            exit()