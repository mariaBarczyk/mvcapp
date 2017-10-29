


def main():

    model = ToDoList()
    view = View()
    controller = Controller(model, view)

    while True:
        user_choice = int(input('Select an option: '))
        if user_choice == 0:
            controller.add_task()
        elif user_choice == 1:
            controller.modify_task()
        elif user_choice == 2:
            controller.remove_task()
        elif user_choice == 3:
            controller.mark_task()
        elif user_choice == 4:
            controller.display_all_tasks()
            input()
        elif user_choice == 5:
            contrroler.display_single_task()

if __name__ == '__main__':
    main()