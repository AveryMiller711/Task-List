import os, random, sys, time, pickle
os.system('clr')

class to_do_list:

    #recieves an input of priority level and prints related list
    # - either low or high priority
    def print_list(self, priority_level):
        for i in range(len(priority_level)):
            print(str(i + 1) + '. ' + priority_level[i])
            if len(priority_level) == 0:
                print('   None')

    #prints to do list - a go to function
    def print_to_do(self):
        print('\n' * 10)
        print('\n' * 10)
        print('\n' * 10)
        print('\n' * 10)
        print( name + '\'s' + ' To Do List:')
        print('')
        print('Top Priority')
        self.print_list(top_priority)
        print('')
        print('Low Priority')
        self.print_list(additional)

    #Used with help command - lists possible commands
    def list_of_commands(self):
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

    #adds task
    def add(self, priority_level):
        print('Enter the task to be added')
        new_task = input()
        
        return priority_level.append(new_task)

    #remove task
    def remove(self, priority_level):
        if len(priority_level) == 0:
            print('There\'s nothing to be removed')
            time.sleep(3)
        else:
            print('Enter the number of the task to be removed')
            removed_task = int(input())
            return priority_level.remove(priority_level[removed_task - 1])

    #what happens when you finish a task - checking it off the list
    def completed(self, priority_level):
        if len(priority_level) == 0:
            print('There\'s nothing to be completed')
            time.sleep(3)
        else:
            print('Enter the number of the task completed')
            removed_task = int(input())
            if priority_level == top_priority:
                print('Yay! You completed top priority task number ' + str(removed_task) + '!')
            else:
                print('Yay! You completed additional task number ' + str(removed_task) + '!')
        time.sleep(3)
        return priority_level.remove(priority_level[removed_task - 1])

    
    def move(self, start_list, end_list):
        print('Enter the task number to move')
        moved_task = int(input())
        task = start_list[moved_task - 1]
        return start_list.remove(task), end_list.append(task)

    #change a task
    def edit(self, priority_level):
        print('Enter the task number to edit')
        task_index = int(input()) - 1
        task = priority_level[task_index]
        print('Original task: ' + task)
        print('Enter your edit:')
        new_task = input()
        priority_level[task_index] = new_task
        return priority_level

    #gets a random quote
    def quote(self):
        lines = open('quotes.txt').read().splitlines()
        myline = random.choice(lines)
        time.sleep(1)
        print('\n\"' + myline + '\"')








#"main"
  

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

user = to_do_list()
user.print_to_do()

while True:
    print('\n' * 10)
    print('Waiting for command')
    print('Enter \'help\' for list of commands')
    command = input()
    if command == 'help':
        user.list_of_commands()
    elif command == 'list':
        user.print_to_do()
    elif command == 'add priority':
        user.add(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        user.print_to_do()
    elif command == 'add additional':
        user.add(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        user.print_to_do()
    elif command == 'remove priority':
        user.remove(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        user.print_to_do()
    elif command == 'remove additional':
        user.remove(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        user.print_to_do()
    elif command == 'complete priority':
        user.completed(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        user.print_to_do()
    elif command == 'complete additional':
        user.completed(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        user.print_to_do()
    elif command == 'move priority to additional':
        user.move(top_priority, additional)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        pickle.dump(additional, open('add.dat', 'wb'))
        user.print_to_do()
    elif command == 'move additional to priority':
        user.move(additional, top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        pickle.dump(additional, open('add.dat', 'wb'))
        user.print_to_do()
    elif command == 'edit priority':
        user.edit(top_priority)
        pickle.dump(top_priority, open('top.dat', 'wb'))
        user.print_to_do()
    elif command == 'edit additional':
        user.edit(additional)
        pickle.dump(additional, open('add.dat', 'wb'))
        user.print_to_do()
    elif command == 'quote':
        user.quote()
    elif command == 'quit':
        print('Goodbye ' + name + '!')
        time.sleep(1)
        sys.exit()
    else:
        print('Oops! There is no \'' + command + '\' command.')
        time.sleep(2)
    
