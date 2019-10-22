import os, random, sys, time, pickle
os.system('clr')

def print_list(some_list):
    for i in range(len(some_list)):
        print(str(i + 1) + '. ' + some_list[i])
    if len(some_list) == 0:
        print('   None')

def print_to_do():
    print('\n' * 10)
    print('\n' * 10)
    print('\n' * 10)
    print('\n' * 10)
    print( name + '\'s' + ' To Do List:')
    print('')
    print('Top Priority')
    print_list(top_priority)
    print('')
    print('Additional')
    print_list(additional)

def list_of_commands():
    print('')
    print(' --------------------------------------------------------------')
    print('|Print To Do List: \'list\'                                      |')
    print('|Add a task: \'add priority\\additional\'                         |')
    print('|Remove a task: \'remove priority\\additional\'                   |')
    print('|Complete a task: \'complete priority\\additional\'               |')
    print('|Move a task: \'move priority\\additional to additional\\priority\'|')
    print('|Edit a task: \'edit priority\\additional\'                       |')
    print('|Motivational Quote: \'quote\'                                   |')
    print('|End Program: \'quit\'                                           |')
    print(' --------------------------------------------------------------')

def add(some_list):
    print('Enter the task to be added')
    new_task = input()
    return some_list.append(new_task)

def remove(some_list):
    if len(some_list) == 0:
        print('There\'s nothing to be removed')
        time.sleep(3)
    else:
        print('Enter the number of the task to be removed')
        removed_task = int(input())
        return some_list.remove(some_list[removed_task - 1])

def completed(some_list):
    if len(some_list) == 0:
        print('There\'s nothing to be completed')
        time.sleep(3)
    else:
        print('Enter the number of the task completed')
        removed_task = int(input())
        if some_list == top_priority:
            print('Yay! You completed top priority task number ' + str(removed_task) + '!')
        else:
            print('Yay! You completed additional task number ' + str(removed_task) + '!')
        time.sleep(3)
        return some_list.remove(some_list[removed_task - 1])

def move(start_list, end_list):
    print('Enter the task number to move')
    moved_task = int(input())
    task = start_list[moved_task - 1]
    return start_list.remove(task), end_list.append(task)

def edit(some_list):
    print('Enter the task number to edit')
    task_index = int(input()) - 1
    task = some_list[task_index]
    print('Original task: ' + task)
    print('Enter your edit:')
    new_task = input()
    some_list[task_index] = new_task
    return some_list

def quote():
    lines = open('quotes.txt').read().splitlines()
    myline = random.choice(lines)
    time.sleep(1)
    print('\n\"' + myline + '\"')
    

try:
    name = pickle.load(open('namesave.dat', 'rb'))
    top_priority = pickle.load(open('top.dat', 'rb'))
    additional = pickle.load(open('add.dat', 'rb'))
    print('Welcome back ' + name + '!')
    time.sleep(3)
except:
    top_priority = []
    additional = []
    pickle.dump(top_priority, open('top.dat', 'wb'))
    pickle.dump(additional, open('add.dat', 'wb'))
    print('Welcome to Task List! I don\'t believe we\'ve met.')
    print('What should I call you?')
    name = input()
    pickle.dump(name, open('namesave.dat', 'wb'))
    time.sleep(2)
    print('It\'s nice to meet you ' + name + '!')
    print('Let\'s get started!')
    time.sleep(5)

print_to_do()
while True:
    print('\n' * 10)
    print('Waiting for command')
    print('Enter \'help\' for list of commands')
    command = input()
    if command == 'help':
        list_of_commands()
    elif command == 'list':
        print_to_do()
    elif command == 'add priority':
        add(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        print_to_do()
    elif command == 'add additional':
        add(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'remove priority':
        remove(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        print_to_do()
    elif command == 'remove additional':
        remove(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'complete priority':
        completed(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        print_to_do()
    elif command == 'complete additional':
        completed(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'move priority to additional':
        move(top_priority, additional)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'move additional to priority':
        move(additional, top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'edit priority':
        edit(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        print_to_do()
    elif command == 'edit additional':
        edit(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'quote':
        quote()
    elif command == 'quit':
        print('Goodbye ' + name + '!')
        time.sleep(1)
        sys.exit()
    else:
        print('Oops! There is no \'' + command + '\' command.')
        time.sleep(2)
    

