class ToDoTask:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_done = is_done

    def mark_task(self):
        task.is_done = True

    def generate_id(self):
        tasks_id = []
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        while True:
            first_part = random.choice(symbols)
            print(first_part)
            second_part = random.choice(string.ascii_letters)
            id = first_part + second_part
            if id not in tasks_id:
                tasks_id.append(id)
                return id


class ToDoList:

    def __init__(self):
        self.to_do_list = []

    def add_task(self, name, description):
        task = ToDoTask(name, description)
        self.to_do_list.append(task)

    def remove_task(self, task):
        self.to_do_list.remove(task)

    def modify_task_name(self, task, new_name):
        task.name = new_name

    def modify_task_description(self, task, new_description):
        task.description = new_description
