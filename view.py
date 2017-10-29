
MENU_OPTIONS = ['Add task', 'Modify task', 'Remove task',
                'Mark task', 'Display task list', 'Display task details']


class View:

    def display_menu():
        print('Welcome in ToDo application')
        for option in MENU_OPTIONS:
            print(str(MENU_OPTIONS.index(option)) + ". " + option)
