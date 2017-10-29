MENU_OPTIONS = ['Add task', 'Modify task', 'Remove task',
                'Mark task', 'Display task list', 'Display task details']


class View:

    def display_menu():
        print('Welcome in ToDo application')
        for option in MENU_OPTIONS:
            print(str(MENU_OPTIONS.index(option) + 1) + ". " + option)

    def display_all_tasks(self, table):
        print(table)

    def display_task_details(self, task_details):
        print(task_details)

    def display_wrong_lenght_msg(self):
        print('To long! name < 20 and description < 150 characters.')

    @staticmethod
    def display_wrong_task_name():
        print('Wrong task name.')
