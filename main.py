import os
from controller import Controller
from view import View
from model import ToDoList


def main():

    model = ToDoList()
    view = View()
    controller = Controller(model, view)

    while True:
        os.system('clear')
        View.display_menu()
        user_choice = int(input('Select an option: '))
        os.system('clear')
        if user_choice == 1:
            controller.add_task()
        elif user_choice == 2:
            controller.modify_task()
        elif user_choice == 3:
            controller.remove_task()
        elif user_choice == 4:
            controller.mark_task()
        elif user_choice == 5:
            controller.display_all_tasks()
            input()
        elif user_choice == 6:
            controller.display_task_details()
            input()
        os.system('clear')


if __name__ == '__main__':
    main()
