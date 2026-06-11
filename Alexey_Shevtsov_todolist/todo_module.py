class BadIdError(Exception):
    """Класс для обработки ошибок неверно введенного индекса."""

    def __init__(self, id, message):
        self.id = id
        self.message = message
    
    def __str__(self):
        return f'BadIdError: id: {self.id}, message: {self.message}'


class BadNameError(Exception):
    """Класс для обработки ошибок неверно введенного имени задачи."""

    def __init__(self, name, message):
        self.name = name
        self.message = message
    def __str__(self):
        return f'BadNameError: name: {self.name}, message: {self.message}'


class BadPriorityError(Exception):
    """Класс для обработки ошибок неверно введенного приоритета"""

    def __init__(self, priority, message):
        self.priority = priority
        self.message = message
    
    def __str__(self):
        return f'BadPriorityError: priority: {self.priority}, message: {self.message}'


class Task:
    def __init__(self, tname, tpriority):
        self.tname = tname
        self.tpriority = tpriority

    def __str__(self):
        return f'name: {self.tname} | priority {self.priority}'


class TodoList:
    __auto_id = 1

    def __init__(self):
        self.__task_storage: dict[Task] = {}
    
    @classmethod
    def incrId(cls):
        cls.__auto_id += 1
    
    @classmethod
    def getId(cls):
        return cls.__auto_id
    
    def create(self, name, priority):
        """Метод для добавления задачи в хранилище"""
        if len(name) < 7:
            raise BadNameError(name, 'Имя должно быть более 7 символов')
        
        if priority < 1 or priority > 100:
            raise BadPriorityError(
                priority, 'Приоритет должен быть в диапозоне от 1 до 100'
            )
        
        self.__task_storage.update({TodoList.getId(): Task(name, priority)})
        TodoList.incrId()
        return True
    
    def read(self, tid) -> Task:
        """Метод для чтения задачи по id"""
        if tid < 1:
            raise BadIdError(tid, 'Номер задачи от 1!')

        if tid not in self.__task_storage:
            raise BadIdError(tid, 'Номер задачи не содержится')

        return self.__task_storage.get(tid)

    def read_all(self):
        """Метод для чтения всех задач"""
        res_str = 'Номер задачи: значение\n'
        for k, v in self.__task_storage.items():
            res_str += f'{k} | {v}\n'

        return res_str    

    def update(self, tid, name, priority):
        """Метод для обновления задачи в хранилище"""
        if tid < 1:
            raise BadIdError(tid, 'Номер задачи от 1!')
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, 'Номер задачи не содержится!')
        
        if len(name) < 7:
            raise BadNameError(name, 'Имя должно быть более 7 символов!')
        
        if priority < 1 or priority > 100:
            raise BadPriorityError(
                priority, 'Приоритет должен быть в диапозоне от 1 до 100'
            )
        
        self.__task_storage.update({tid: Task(name, priority)})

        return True
    
    def delete(self, tid):
        """Метод для удаления задачи по id"""
        if tid < 1:
            raise BadIdError(tid, 'Номер задачи от 1!')
        
        if tid not in self.__task_storage:
            raise BadIdError(tid, 'Номер задачи не содержится!')
        
        self.__task_storage.pop(tid)

        return True

class App:
    def __init__(self):
        self.__todolist = TodoList()

    def Run(self):
        condition = input(App.condition_display())
        while condition != '-1':
            try:
                if condition == '1':
                    name = input('Введите name: ')
                    priority = int(input('Введите priority: '))
                    self.__todolist.create(name, priority)
                elif condition == '2':
                    print(self.__todolist.read_all())
                elif condition == '3':
                    tid = int(input('Введите id: '))
                    print(self.__todolist.read(tid))
                elif condition == '4':
                    tid = int(input('Введите id: '))
                    name = input('Введите name: ')
                    priority = int(input('Введите priority: '))
                    self.__todolist.update(tid, name, priority)
                elif condition == '5':
                    tid = int(input('Введите id: '))
                    self.__todolist.delete(tid)
                else:
                    print('Неизвестная операция')
                    print(App.condtion_display())
            except BadIdError as e:
                print("Проблема: ", e)
            except BadNameError as e:
                print("Проблема: ", e)
            except BadPriorityError as e:
                print('Проблема:', e)
            except Exception as e:
                print("Неизвестная проблема!", e)
            else:
                print('Операция прошла успешно')
            
            condition = input("Выберите операцию: ")

        print('This is the end')
        print('Bye bye')

    @staticmethod
    def condition_display():
        return """
        Номер задачи(от 1)
        Имя задачи(не менее 7 символов)
        Приоритет(от 1 до 100)
        1 - create - добавление новой задачи
        2 - read_all - просмотр списка задач
        3 - read - просмотр задачи по id
        4 - update - обновление задачи по id
        5 - delete - удаление задачи по id
        -1 - exit - выход из программы 
        """