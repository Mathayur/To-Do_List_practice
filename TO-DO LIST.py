#List for the tasks
tasks =[]

#Add to list function
def add():
    list_item = input('\nAdd a task: ')
    tasks.append(list_item)
    print('Task added\n')

def remove():
    remove_item = int(input('\nType the task number you want to remove: '))
    if remove_item <= len(tasks):
        final_index = remove_item - 1
        del tasks[final_index]
    else:
        print('This task does not exist.\n')

def edit():
    edit_item = int(input('\nType the task number you want to edit: '))
    if edit_item <= len(tasks):
        real_index = edit_item - 1
        del tasks[real_index]
        new_task = input('Add the new task:')
        tasks.insert(real_index, new_task)
    else:
        print('This task does not exist.\n')

def exit_todolist():
    print('\nExiting Program.\n')
    exit()
    

menu = {
    1:add,
    2:remove,
    3:edit,
    4:exit_todolist
    }

def display_menu():
    final_list = list(enumerate(tasks, start=1))
    for i in final_list:
        print(i)
    
    print('''\n----OPTIONS---- 
        1 = ADD TASK
        2 = REMOVE TASK
        3 = EDIT TASK
        4 = EXIT PROGRAM\n''')
    try:
        user = int(input('Enter the number: '))
        if user == 3 and len(tasks) == 0:
            print('\nTasks are empty.\nChoose another option.')
        elif user in [1,2,3,4]:
            menu[user]()
        else:
            print('\nInvalid choice!\nPlease try again.\n')
    except ValueError:
        print('\nInvalid choice!\nPlease try again.\n')           
while True:
    display_menu()
    
        
        