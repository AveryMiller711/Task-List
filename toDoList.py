import pickle, os, random, sys, time

def print_list(some_list):
    for i in range(len(some_list)):
        print(str(i + 1) + '. ' + some_list[i])
    if len(some_list) == 0:
        print('   None')

def print_to_do():
    print('Your To Do List:')
    print('')
    print('Top Priority')
    print_list(top_priority)
    print('Additional')
    print_list(additional)

def list_of_commands():
    print('')
    print('Add a task: \'add\'')
    print('Remove a task: \'remove\'')
    print('Motivational Quote: \'quote\'')
    print('End Program: \'quit\'')

def add(some_list):
    print('Enter the task to be added')
    new_task = input()
    print('')
    return some_list.append(new_task)

def remove(some_list):
    print('Enter the number of the task to be removed')
    removed_task = int(input())
    print('')
    return some_list.remove(some_list[removed_task - 1])

def quote():
    lines = open('quotes.txt').read().splitlines()
    myline = random.choice(lines)
    time.sleep(1)
    print('\n\"' + myline + '\"')
    time.sleep(4)

top_priority = []

additional = []

print_to_do()


while True:
    print('')
    print('Waiting for command')
    print('Enter \'help\' for list of commands')
    command = input()
    if command == 'help':
        time.sleep(1)
        list_of_commands()
        command = input()
    if command == 'add':
        print('Top priority? [y/n]')
        if input() == 'y':
            add(top_priority)
            print_to_do()
            time.sleep(2)
        else:
            add(additional)
            print_to_do()
            time.sleep(2)
    if command == 'remove':
        print('Top priority? [y/n]')
        if input() == 'y':
            remove(top_priority)
            print_to_do()
            time.sleep(2)
        else:
            remove(additional)
            print_to_do()
            time.sleep(2)
    if command == 'quote':
        quote()
    if command == 'quit':
        sys.exit()
    

