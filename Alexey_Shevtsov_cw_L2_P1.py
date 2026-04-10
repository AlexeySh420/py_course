print(input("Enter your name: "))
x = input()

#type casting

a = 'hello'
b = 100
c = 3.14
d = True
type(a)

age = int(input("Enter your age: "))
print(round(age / 2))

print(isinstance(a,int))

2**3**2 #right to left

name = 'Alexey'
age = '30'
phone = '+3752911111111'
separator = '-'
#userdata = name+separator+age+separator+phone
userdata = f'{name}{separator}{age}{separator}{phone}'
print(userdata)

import keyword
print(keyword.kwlist)
print(dir(keyword.kwlist))

#calculator
a, b = int(input()), int(input())
print(f'{a} + {b} = {a+b}')

