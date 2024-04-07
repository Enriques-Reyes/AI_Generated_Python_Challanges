# Program is a To-do List Manager allowing users to:
# --> Add To-Do's with due dates, priority, and status
# --> Mark To-Do as complete
# --> List To-Do's in sorted order by status, priority, and due date
# --> Remove To-Do's from the list

import json
from datetime import date
from datetime import timedelta


class TodoListManager:
    def __init__(self, file_name='todos.json'):
        self.file_name = file_name
        self.todos_list = self.sort_todos(self.load_todos())

    def load_todos(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_todos(self):
        self.todos_list = sorted(self.todos_list)
        with open(self.file_name, 'w') as file:
            json.dump(self.todos_list, file, indent=4)

    def sort_todos(self, lists):
        # Sorts inserted list by status ['In Progress', then 'Completed'], then by priority [Highest to lowest],
        # and lastly by due date [soonest to latest]
        return sorted(
            lists,
            key=lambda x: (
                0 if x['status'] == 'In Progress' else 1,  # Reverse the status sort by using numerical values
                -x['priority'],  # Reverse the priority sort by negating the value
                x['due date']  # Keep the due date in its natural (ascending) order
            )
        )

    def add_todo(self):
        # This function requests user input, verifies inputs, creates a new todo_dictionary,
        # inserts it into self.todos_list, and saves to todos.json document in json formatting
        while True:     # Validates task_to_add input
            task_to_add = input('Enter task you would like to add [QUIT]: ')
            if task_to_add == 'QUIT':
                break
            elif any(todo['task'] == task_to_add for todo in self.todos_list):   # If task is found in the list,
                print('Task already exists')                                     # move the else statement
                continue
            else:
                while True:     # Validates priority input
                    try:
                        priority = int(input('Enter priority number from 1-10 [1 lower:10 higher]: '))
                        if 1 > priority or priority > 10:
                            print('Invalid Input!!! Enter number between 1 and 10!!!')
                            continue
                        else:
                            break
                    except ValueError:
                        print('Invalid Input!!! Enter number between 1 and 10!!!')
                while True:     # Validates date input
                    try:
                        due_date = str(date.today() + timedelta(days=int(input('Enter number of days till due: '))))
                        break
                    except ValueError:
                        print('Invalid Input!!! Enter a number!!!')
                new_todo = {
                    'task': task_to_add,
                    'priority': priority,
                    'due date': due_date,
                    'status': 'In Progress'
                }   # End of new_todo dictionary
                self.todos_list.append(new_todo)
                self.save_todos()
                print('Todo added!!!')
                break

    def mark_todo_as_complete(self):
        # Marks todos as complete
        while True:
            task_to_mark = input('Enter the task you want to mark as complete [QUIT]: ')
            if task_to_mark == 'QUIT':
                break
            elif not any(todo['task'] == task_to_mark for todo in self.todos_list):
                print('Task not found!!!')
                continue
            else:
                for todo in self.todos_list:
                    if todo['task'] == task_to_mark:
                        todo['status'] = 'Completed'
                        break
                    else:
                        continue
                self.save_todos()
                print('Todo is marked as complete!!!')
                break

    def list_todos(self):
        # List todos [ALL, IN PROGRESS, or COMPLETED]
        while True:
            answer = input('Enter what you would like to list [ALL, In Progress, Completed, QUIT] ')
            if answer in ['ALL', 'In Progress', 'Completed', 'QUIT']:
                break
            else:
                print('Invalid input!!! Enter from a list of options [ALL, In Progress, Completed, QUIT]!!!')
                continue
        if answer == 'ALL':
            print(json.dumps(self.todos_list, indent=4))
        elif answer == 'In Progress':
            list_to_display = [todo for todo in self.todos_list if todo['status'] == 'In Progress']
            print(json.dumps(list_to_display, indent=4))
        elif answer == 'Completed':
            list_to_display = [todo for todo in self.todos_list if todo['status'] == 'Completed']
            print(json.dumps(list_to_display, indent=4))

    def remove_todo(self):
        while True:
            task_to_remove = input('Enter task you would like to remove [QUIT]: ')
            if task_to_remove == 'QUIT':
                break
            elif not any(todo['task'] == task_to_remove for todo in self.todos_list):
                print('Task not found!!!')
                continue
            else:
                for todo in self.todos_list:
                    if todo['task'] == task_to_remove:
                        self.todos_list.remove(todo)
                        self.save_todos()
                        print('Removal complete!!!')
                        break
                    else:
                        continue
                break


def main():
    todo_start = TodoListManager()
    print(json.dumps(todo_start.load_todos(), indent=4))
    actions = {
        'ADD': lambda: todo_start.add_todo(),
        'MARK': lambda: todo_start.mark_todo_as_complete(),
        'LIST': lambda: todo_start.list_todos(),
        'REMOVE': lambda: todo_start.remove_todo()
    }
    print('''This program allows you to manage your todos using and number of function. 
[Todos will be saved in the todos.json file]
    
--> ADD: Add todos to the list
--> MARK: Mark todos as complete
--> LIST: List todos [ALL, In Progress, or Completed]
--> REMOVE: Remove todos from the list
    
    ''')
    while True:
        action = input('Enter function you would like to complete [ADD, MARK, LIST, REMOVE, QUIT]: ')
        if action == 'QUIT':
            break
        elif action in actions:
            actions[action]()
        else:
            print('Invalid function!!! Try again!!!')


if __name__ == '__main__':
    main()
