import time

#25-03-2026

print(1,2,3,4, sep='=')

age = 99
print(age)

isinstance(age, bool)

number = input("enter the value: ")
type(number)

int(number)
number / 9

name="alexey"
name*7


password = "12345"

if password =="12345":
    print("passed")
else:
    print('declined')


age = 16

if age <=6:
    print("infant")
elif age <= 16:
    print("teenager")
else:
    print("adult")

#singlline condition

key = 777

if key == "777":
    print(1)
else:
    print(2)

check = True if key == "777" else False


x, y = int(input("x: ")), int(input("y: "))
result= 0

if x > y:
    result = x
else:
    result = y
print(result)

x, y = int(input("x: ")), int(input("y: "))
result= x if x > y else y
print(result)
print(x if x > y else y)

a = 10 

match a:
    case 10:
        print(100)
    case 15:
        print(150)
    case 20:
        print(200)


match a :
    case age if age < 10:
        print(100)
    case age if age == 10:
        print(1000)



# while
x = 5
counter = 1

while counter <= 5:
    print(x)
    counter += 1


# for

for x in range(1, 10):
    print(x, end=' ')

print("\n")

for x in range(1, 10, 2):
    print(x, end=' ')

print("\n")

for i in range(1, 11):
    print(i**2 + (i+i)**2 - i*(i+i+i))

for i in range(5):
    time.sleep(1)
    print(i)

# break continue

for i in range(5):
    if i == 3:
        break
    print(i)

# in not in
x = "test"
"a" in x
"e" in x

# lower title
name = "ASDFG"
name.lower()
name.title

# and or not
name = "x"
phone = "123"
age = 18

if name == "x" and phone == "123" and age == 18:
    print("all matched")
if name == "x" or phone == "123" or age == 18:
    print("some matched")