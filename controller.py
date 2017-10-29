from prettytable import PrettyTable


class Controler:

    MAX_LEN_NAME = 20
    MAX_LEN_DESCRIPTION = 150

    def __init__(self, Model, View):
        self.Model = Model
        self.View = View

    def check_if_task_can_be_created(self, name, description):
        if len(name) > self.MAX_LEN_NAME or len(description) > self.MAX_LEN_DESCRIPTION:
            return False
        return True

    def add_task(self):
        name = input('Enter task name: ')
        description = input('Enter task descritpion: ')
        if self.check_if_task_can_be_created(name, description):
            self.Model.add_task(name, description)
        else:
            View.display_message()

    def remove_task(self):
        task_name = input('Enter task name to delete: ')
        task = self.search_task_by_name(task_name)
        self.Model.remove_task(task)

    def modify_task(self):
        user_choice = int(input('Press 1 to modify name or 2 to modify description: '))
        if user_choice == 1:
            self.modify_task_name()
        elif user_choice == 2:
            self.modify_task_desription()
        else:
            View.display_message()

    def modify_task_name(self):
        task_name = input('Enter task name: ')
        new_name = input('Enter new task name: ')
        task = self.search_task_by_name(task_name)
        self.Model.modify_task_name(task, new_name)

    def modify_task_desription(self):
        task_name = input('Enter task name: ')
        new_description = input('Enter new task description: ')
        task = self.search_task_by_name(task_name)
        self.Model.modify_task_description(task, new_description)