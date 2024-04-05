# Program is a To-do List Manager allowing users to:
# --> Add To-Do's with due dates, priority, and status
# --> Mark To-Do as complete
# --> List To-Do's in sorted order by priority, status, and due date
# --> Remove To-Do's from the list

import json
from datetime import date
from datetime import timedelta


class TodoListManager:
    def __init__(self, file_name='todos.json'):
        self.file_name = file_name
        self.todos_list = self.load_todos()

    def load_todos(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_todos(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.todos_list, file, indent=4)

    def add_todo(self, task, completion_status='In Progress'):
        # This function requests user input, verifies inputs, creates a new todo_dictionary,
        # inserts it into self.todos_list, and saves to todos.json document in json formatting
        if any(todo['task'] == task for todo in self.todos_list):   # If task is found in the list,
            print('Task already exists')                            # move the else statement
        else:
            while True:
                try:
                    priority = int(input('Enter priority number from 1-10 [1 lower:10 higher]: '))
                    if 1 > priority or priority > 10:
                        print('Invalid Input!!! Enter number between 1 and 10!!!')
                        continue
                    else:
                        break
                except ValueError:
                    print('Invalid Input!!! Enter number between 1 and 10!!!')
            while True:     #
                try:
                    due_date = str(date.today() + timedelta(days=int(input('Enter number of days till due: '))))
                    break
                except ValueError:
                    print('Invalid Input!!! Enter a number!!!')
            new_todo = {
                'task': task,
                'priority': priority,
                'due date': due_date,
                'status': completion_status
            }   # End of new_todo dictionary
            self.todos_list.append(new_todo)
            print(self.todos_list)
            self.save_todos()

    def mark_todo_as_complete(self, task):
        if not any(todo['task'] == task for todo in self.todos_list):
            print('Task not found!!!')
        else:
            for todo in self.todos_list:
                if todo['task'] == task:
                    todo['status'] = 'Completed'
                    print('Starting!')
                    break
                else:
                    continue
            self.save_todos()
            print('Todo is marked as complete!!!')

    def remove_todo(self, task):
        print(self.todos_list[0]['task'])
        if not any(todo['task'] == task for todo in self.todos_list):
            print('Task not found!!!')
        else:
            print(todo for todo in self.todos_list if todo['task'] == task)
            for todo in self.todos_list:
                if todo['task'] == task:
                    self.todos_list.remove(todo)
                    self.save_todos()
                    print('Removal complete!!!')
                    break
                else:
                    continue


todo_start = TodoListManager()
# todo_start.add_todo(input('Enter task: '))
# todo_start.mark_todo_as_complete(input('Enter task: '))
todo_start.remove_todo(input('Enter task to remove: '))
# print(date.today())
