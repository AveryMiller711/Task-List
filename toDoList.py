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
    print(' ----------------------------')
    print('|Print To Do List: \'list\'    |')
    print('|Add a task: \'add\'           |')
    print('|Remove a task: \'remove\'     |')
    print('|Completed a task: \'complete\'|')
    print('|Motivational Quote: \'quote\' |')
    print('|End Program: \'quit\'         |')
    print(' ----------------------------')

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
    elif command == 'add':
        print('Is it a top priority? [y/n]')
        if input() == 'y':
            add(top_priority)
            pickle.dump(top_priority, open('top.dat', 'wb'))
        else:
            add(additional)
            pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'remove':
        print('Is it a top priority? [y/n]')
        if input() == 'y':
            remove(top_priority)
            pickle.dump(top_priority, open('top.dat', 'wb'))
        else:
            remove(additional)
            pickle.dump(additional, open('add.dat', 'wb'))
        print_to_do()
    elif command == 'complete':
        print('Is it a top priority? [y/n]')
        if input() == 'y':
            completed(top_priority)
            pickle.dump(top_priority, open('top.dat', 'wb'))
        else:
            completed(additional)
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
    

