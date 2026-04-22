# # tuple
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(type(li), type(set), type(tuple))
# # tuple can also be created
# a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 # that's tuple
# tuple1 = ()
# print(tuple1)
# tuple2 = 0.,1.0,.2
# print(tuple2)
# tuple3 = (999,) + tuple2[1:]
# tuple3 = list(tuple3)
#
# def useful(n):
#     tt = ()
#     for i in range(n):
#         tt = tt + (i,)
#     return tt
#
# print(useful(4))
#
# result = useful(4)
# len(result)
# a, b, c, d = useful(4)
# _, b, c, _ = useful(4)
# print(b, c)
#
# print(tuple + tuple2)
#
# # dictionary
# dict = {1:"one", 2:"two", 3:"three"}
#
# di = {
#     "name": "Alexey",
#     "age": 30,
#     "phone": 123456789
# }
#
# print(di.get("name"))
# #or
# print(di["name"])
#
# print(di)
#
# print(di.values(),"\n", di.keys())
#
# for k, v in di.items():
#     print(k,v)
#
# di.update({"age": 19})
# print(di)
#
# di.update([("1", 1), ("2", 12), ("3", 13), ("4", 14)])
# print(di)
#
# di.pop("name")
# print(di)
#
# print("phone" in di)
#
# # Lab 6 ToDo list
# def create_task(max_id):
# auto_id = max_id + 1
#
# todo = input("todo:")
# completed = bool(input("completed:"))
# userId = int(input("userId:"))
# priority = int(input("priority:"))
#
# new_task = {auto_id:{
# "todo": todo,
# "completed": completed,
# "userId": userId,
# "priority": priority,
# }
# }
# return new_task
#
#
#
# # CRUD
# # хранить задачи - ок
# # добавить задачу - ок create
# # печатать задачи - ок read
# # Обновляем +- update
# # удалить - ок delete
#
# # менюшка
# # общая функция с циклом внутри и тп
#
#
# def create_task(max_id):
# auto_id = max_id + 1
#
# todo = input("todo:")
# completed = bool(input("completed (1 Для True, пустой ввод для False):"))
# userId = int(input("userId:"))
# priority = int(input("priority:"))
#
# new_task = {auto_id:{
# "todo": todo,
# "completed": completed,
# "userId": userId,
# "priority": priority,
# }
# }
#
# return new_task
#
#
# def read_tasks():
# for tk, tdi in todos.items():
#
# print("Task id:", tk)
#
# for k, v in tdi.items():
# print(" ", k, ":", v)
# print("__________________________________")
#
#
# def read_task(tid):
# res_task = todos.get(tid, -1)
#
# if res_task == -1:
# print("задача не найдена с id:", tid)
# return
#
# print("Task id:", tid)
#
# for k, v in res_task.items():
# print(" ", k, ":", v)
#
# print("__________________________________")
#
#
# def delete_task(tid):
# res_task = todos.get(tid, -1)
#
# if res_task == -1:
# print("задача не найдена с id:", tid)
# return
#
# print("Task id:", tid)
# todos.pop(tid)
#
# print("задача с id:", tid, "удалена.")
# print("__________________________________")
#
#
# todos = {
# 1:{
# "todo": "Do something nice for someone you care about",
# "completed": False,
# "userId": 152,
# 'priority': 5
# },
# 2: {
# "todo": "Memorize a poem",
# "completed": True,
# "userId": 13,
# 'priority': 5
# },
# 3: {
# "todo": "Watch a classic movie",
# "completed": True,
# "userId": 68,
# 'priority': 5
# },
# }
#
#
# def main():
# print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
# operation = int(input("-->"))
#
# while operation != 5:
# if operation == 1:
# task = create_task(max(todos.keys()))
# todos.update(task)
# elif operation == 2:
# tid = int(input("Введи таск id:"))
# read_task(tid)
# elif operation == 3:
# read_tasks()
# elif operation == 4:
# tid = int(input("Введи таск id:"))
# delete_task(tid)
# else:
# print("я не понял попробуй ещё раз.")
#
# print("1 - create, 2 read task by id, 3 reat all tasks, 4 delete task by id, 5 exit")
# operation = int(input("-->"))
#
# print("пока пока")
#
#
# main()
#


# # 10.04.2026 Lecture 5
import time
time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

# import calendar as c
# from calendar import isleap
# from calendar import *
import calendar
calendar.isleap(2010)

import random as r
def game()
    rand_number = r.randint(0, 3) # randon number from 1 to 3
    user_number = int(input("Enter a number between 1 and 3: "))

    if user_number == rand_number:
        print("ok")
    else:
        print("not ok")

game()