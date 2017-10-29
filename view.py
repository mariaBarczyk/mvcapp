MENU_OPTIONS = ['Add task', 'Modify task', 'Remove task',
                'Mark task', 'Display task list', 'Display task details']


class View:

    def display_menu():
        print('Welcome in ToDo application')
        for option in MENU_OPTIONS:
            print(str(MENU_OPTIONS.index(option)) + ". " + option)

    def display_all_tasks(self, table):
        print(table)

    def display_message(self):
        print('Wrong input')
