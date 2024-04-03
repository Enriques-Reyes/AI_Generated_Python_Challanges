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
