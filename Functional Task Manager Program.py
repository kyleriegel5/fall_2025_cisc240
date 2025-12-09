# Functional Task Manager Program
# 1. Create task
# 2. Add task to list
# 3. Mark task complete
# 4. Display tasks with their status

task_list = []

def create_task():
    task_id = input('Enter Task ID: ')
    task_name = input('Enter Task Name: ')
    status = 'Incomplete'

    task = f'Task ID: {task_id}, Task Name: {task_name}, Status: {status}\n'
    task_list.append(task)

def task_complete():
    print('What task ID would you like to mark complete?')

    # Prints full tasks, want only Task ID's
    for task_id in task_list:
        print (task_id)

    complete = input(">>> ")

    # Since the for loop above prints full tasks, this variable and if statement won't work
    taskID_list = [task for task in task_list if task_id == complete]
    if taskID_list:
        status = 'Complete'
        print(f'Task ID {task_id} is now marked {status}!')
    else:
        print(f'{complete} is not a task ID in the Task Manager.')

    
def display_tasks():
    for task in task_list:
        print(task)

menu = '0'
while menu != '4':
    menu = input(
    "Please select an option from the Task Manager Menu:\n"
    "1. Create a task\n"
    "2. Mark a task complete\n"
    "3. Display all tasks\n"
    "4. Quit\n"
    ">>> "
    )

    if menu == '1':
        create_task()
    
    elif menu == '2':
        task_complete()

    elif menu == '3':
        display_tasks()

    elif menu == '4':
        print('Goodbye')
        break

    else:
        print('Invalid input.')
