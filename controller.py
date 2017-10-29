class Controler:

    def __init__(self):
        pass

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