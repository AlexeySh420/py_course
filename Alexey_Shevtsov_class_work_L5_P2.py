# # functions
# def summary(a, b):
#     return a + b
# print(summary(1, 66))
#
# def subtract(a, b):
#     return a - b
# print(subtract(1, 66))
#
#
# # Caesar Cypher
# def main():
#     runApp()
#
#
# def runApp():
#     user_input = int(input("1 - cypher, 2 - decypher, 0 - exit"))
#     while user_input != 0:
#         key = int(input("Enter key: "))
#         msg = give_me_message()
#         if user_input == 1:
#             cyphered = cypher(msg, key)
#             print(cyphered)
#         elif user_input == 2:
#             print(decypher(msg, key))
#         else:
#             print("Invalid Input")
#
#         user_input = int(input("1 - cypher, 2 - decypher, 0 - exit"))
#
#
# def give_me_message():
#     message = input()
#     return message
#
#
# def cypher(message, key):
#     secured_message = ""
#     for i in message:
#         secured_message += chr(ord(i) + key)
#     return secured_message
#
#
# def decypher(cyphered, key):
#     x = ""
#     for i in cyphered:
#         x += chr(ord(i) - key)
#     return x
#
#
# if __name__ == "__main__":
#     main()
#

# def hello(name="-", surname, phone, age, email):
#     print("Hello, " + name, surname, phone, age, email)

# def empty():
#     pass
# print(empty())
#
# def mul(a, b):
#     """
#     this function is used to multiply two numbers
#     """
#     res = a * b
#     return res
# help(mul)
#
# copy_mul = mul
# #del(mul)
# print(copy_mul(4, 5))
#
# list = [1, 2, 3, 4, 5, 6]
# list2 = list
# print(list is list2)
#
# def check_age(age):
#     if age > 18:
#         return True
#     else:
#         return False
#
# print(check_age(19))
#
# def check_age(age):
#     return age > 18
#
# inner_list = [1, 2, 3, 4, 5, 6]
# def swap(inner_list):
#     inner_list[2] = 99999
#     return inner_list
#
# print(swap(inner_list))
#
# # Local Global variables
# def h(n):
#     n = 99
#     print(n)
#     n = "test"
#     print(n)
# h(11)
#
# # global variable
# age = 18
# def grow(y):
#     global age
#     age = age + y
#     return age
# print(grow(10))

# factorial
n = 5
def my_factorial(n):
    if n < 0:
        return None
    if n <= 1:
        return 1

    targetValue = 1
    for i in range(2, n+1):
        targetValue *= i

    return targetValue

list12 = [-999, 0, 1, 9, 2, 5]
list123 = [False, 1, 1, 362880, 2, 120]

for number, result in zip(list12, list123):
    if my_factorial(number) == result:
        print("ok")
    else:
        print("failed")
        print("Expected: ", number, result)
        print("Actual: ", number, my_factorial(number))

# recursion
j = 10
def fun(j):
    if j >= 0:
        return fun(j - 1)
    if j < 0:
        return j
print(fun(j))

