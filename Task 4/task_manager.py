class Task:
    def __init__(self, id, name, description, status):
        self.__id = id
        self.__name = name
        self.__description = description
        self.status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f' id: {self.__id}\n name: {self.__name}\n description: {self.__description}\n status: {self.status}'


class Subtask(Task):
    def __init__(self, id, name, description, status, parent_id):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id

    def __str__(self):
        return super().__str__() + f'\n parent_id: {self.parent_id}'


class ComplexTask(Task):
    def __init__(self, id, name, description, status, subtasks):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks

    def __str__(self):
        subtasks_list = ''
        for subtask in self.subtasks:
            subtasks_list += f'\n {subtask}'
        return super().__str__() + subtasks_list


class TaskManager:
    id_series = 1

    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
        self.complex_tasks = {}

    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value

    def create_task(self, name, description, status):
        current_id = self.__get_and_increment_id()
        task = Task(current_id, name, description, status)
        self.tasks[current_id] = task
        return task

    def create_subtask(self, name, description, status, parent_id):
        id_subtask = self.__get_and_increment_id()
        subtask = Subtask(id_subtask, name, description, status, parent_id)
        self.subtasks[id_subtask] = subtask
        return subtask

    def create_complex_task(self, name, description, status, subtasks):
        id_complex_task = self.__get_and_increment_id()
        complex_task = ComplexTask(id_complex_task, name, description, status, subtasks)
        self.complex_tasks[id_complex_task] = complex_task
        return complex_task

    def get_tasks(self):
        res=''
        for task in self.tasks.values():
            res+= f'{task}\n'
        print(res)

    def get_subtasks(self):
        res=''
        for subtask in self.subtasks.values():
            res+= f'{subtask}\n'
        print(res)

    def get_complex_tasks(self):
        res=''
        for complex_task in self.complex_tasks.values():
            res+= f'{complex_task}\n'
        print(res)

    def get_tasks_by_id(self, id):
        print(self.tasks[id])

    def get_subtasks_by_id(self, id):
        print(self.subtasks[id])

    def get_complex_tasks_by_id(self, id):
        print(self.complex_tasks[id])

    def remove_tasks(self):
        self.tasks = {}

    def remove_subtasks(self):
        self.subtasks = {}

    def remove_complex_tasks(self):
        self.complex_tasks = {}

    def remove_task_by_id(self, id):
        self.tasks.pop(id)

    def remove_subtask_by_id(self, id):
        self.subtasks.pop(id)

    def remove_complex_task_by_id(self, id):
        self.complex_tasks.pop(id)

    def update_status(self, id, updated_status):
        self.tasks[id].status = updated_status
    
def main():
    result = TaskManager()
    result.create_task("Cleaning", "Мake the flat clean", 'In progress')
    result.create_subtask("Кitchen", "Wash the dishes", 'In progress',1)
    result.create_subtask("Bath", "Wash wash the bath and toilet", 'In progress',1)
    result.create_subtask("Room", "Make the bed", 'In progress',1)
    result.create_task("Products", "Buy goods in the store", 'In progress')
    result.get_tasks()
    result.get_subtasks()
    result.create_complex_task('My tasks','Tasks for me','In progress',['HW','Nails'])
    result.get_complex_tasks()
    result.update_status(5,'Done')
    result.get_tasks()
    result.remove_complex_task_by_id(6)
    result.get_complex_tasks()
if __name__ == "__main__":
    main()