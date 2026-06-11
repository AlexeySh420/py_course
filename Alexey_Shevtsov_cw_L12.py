# L12 04.24.2026

# class A:
#     def __init__(self, aa, bb):
#         self.aa = aa
#         self.bb = bb

# aaaa = A(11, 22)
# aaaa.aa

# aaaa.bb = 999



import sys

class A:
    def __init__(self, aa, bb):
        self._aa = aa
        self._bb = bb

    @property
    def aa(self):
        print("Сработал метод getter")
        return self._aa

    @aa.setter
    def aa(self, value):
        print("Сработал метод setter")
        self._aa = value
        print("Значение которое устанавливается", value)

    @property
    def bb(self):
        print("Сработал метод getter")
        return self._b

    @bb.setter
    def bb(self, value):
        print("Сработал метод setter")
        self._bb = value
        print("Значение которе устанавливается", value)
aaaaaaaaa = A(11, 12)
aaaaaaaaa.aa = 88888



def hhh(*args):  # return sets accepts values and
    return args


def my_print(*args, sep=" ", end="\n"):
    for i in args:
        print(i, end=sep)
    print(end=end)
di = {"A": 10, "B": 11, "C": 12}


def user(**kwargs):
    return kwargs
u1 = user(name="dima", age=20)
print(u1)



def my_match(a, b, c):
    b(lambda n: b * 2 / n**5 % 7 / n * 100)(b)
    return a * b * c



class Tasks:
    def __init__(self):
        self.tasks = []

    def __iter__(self):
        return iter(self.tasks)


tt = Tasks()
tt.tasks.append("t1")
tt.tasks.append("t2")
tt.tasks.append("t3")

for task in tt:
    print(task)


class Task:
    def __init__(self, tname, tprior):
        self.tname = tname
        self.tprior = tprior

    def __str__(self):
        return f"{self.tname} | {self.tprior}"


class Tasks:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        self.tasks.append(task)


    def __iter__(self):
        return iter(self.tasks)



# Generator
def n(x):
    for i in range(x):
        yield i


user_number = 10
for val in n(user_number):
    print(val, end=" ")


# infinite iterator
def g():
    i = 0
    while True:
        yield i
        i += 1


# Dynamic Class generator
class Tasks(list):
    def my_append(self, value):
        print("добавляю в список значение", value)
        self.append(value)

    def my_pop(self):
        if len(self) == 0:
            print("Список пуст")
            return
        res = self.pop()
        print("удаляю значение из списка", res)


My_tasks = type(
    "My_tasks",
    (list,),
    dict(
        my_append=lambda self, value: self.append(value),
        my_pop=lambda self: self.pop(),
    ),
)
