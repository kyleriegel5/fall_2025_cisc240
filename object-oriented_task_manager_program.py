# Object-Oriented Task Manager Program
# 1. Create task
# 2. Add task to list
# 3. Mark task complete
# 4. Display tasks with their status

class Task:
    # How do I make task_id unique, and only accept int?
    def __init__(self, task_id, task_name, status):
        self.task_id: int = task_id
        self.task_name: str = task_name
        self.status: str = status
    
    def set_complete(self):
        self.status = 'Complete'
        return print(f'{self.task_name} is now marked {self.status}!')
    
    def __str__(self):
        return f'Task ID: {self.task_id}, Task Name: {self.task_name}, Status: {self.status}\n'

task_list = []
menu = 0
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
        Task.task_id = input('Enter Task ID: ')
        Task.task_name = input('Enter task name: ')
        Task.status = 'Incomplete'

        task = Task(Task.task_id, Task.task_name, Task.status)
        task_list.append(task)
    
   
    elif menu == '2':
        print('What task ID would you like to mark complete?')
        for task in task_list:
            print(task.task_id)

        complete = input(">>> ")
        # Can do this differently
        taskID_list = [task for task in task_list if task.task_id == complete]

        if taskID_list[0].status == 'Complete':
            print('This task has already been completed.')

        else:
            if taskID_list:
                taskID_list[0].set_complete()
            else:
                print(f'{complete} is not a task ID in the Task Manager.')

    elif menu == '3':
        for task in task_list:
            print(task)

    elif menu == '4':
        print('Goodbye')
        break

    else:
        print('Invalid input.')
