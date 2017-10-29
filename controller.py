from prettytable import PrettyTable


class Controller:

    MAX_LEN_NAME = 20
    MAX_LEN_DESCRIPTION = 150

    def __init__(self, Model, View):
        self.Model = Model
        self.View = View

    def check_if_task_can_be_created(self, name, description):
        if len(name) > self.MAX_LEN_NAME or len(description) > self.MAX_LEN_DESCRIPTION:
            return False
        return True

    def search_task_by_name(self, task_name):
        for task in self.Model.to_do_list:
            if task.name == task_name:
                return task
        self.View.display_message()
        input()

    def add_task(self):
        name = input('Enter task name: ')
        description = input('Enter task descritpion: ')
        if self.check_if_task_can_be_created(name, description):
            self.Model.add_task(name, description)
        else:
            self.View.display_message()

    def remove_task(self):
        task_name = input('Enter task name to delete: ')
        task = self.search_task_by_name(task_name)
        if task:
            self.Model.remove_task(task)

    def mark_task(self):
        task_name = input('Enter task name to mark: ')
        task = self.search_task_by_name(task_name)
        if task:
            task.is_done = True

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
        task = self.search_task_by_name(task_name)
        if task:
            new_name = input('Enter new task name: ')
            self.Model.modify_task_name(task, new_name)

    def modify_task_desription(self):
        task_name = input('Enter task name: ')
        task = self.search_task_by_name(task_name)
        if task:
            new_description = input('Enter new task description: ')
            self.Model.modify_task_description(task, new_description)

    def display_all_tasks(self):
        tasks_table = PrettyTable(['ID', 'NAME', 'DESCRIPTION', 'IS DONE'])
        for task in self.Model.to_do_list:
            tasks_table.add_row([task.id, task.name, task.description, task.is_done])
        self.View.display_all_tasks(tasks_table)

    def display_task_details(self):
        pass
