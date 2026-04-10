# HW 2.1.
x, y, z, n = (
    int(input("Enter a number 1: ")),
    int(input("Enter a number 2: ")),
    int(input("Enter a number 3: ")),
    int(input("Enter a number 4: ")),
)
large_number = 0
large_number2 = 0

# The largest between frist two
large_number = x if x > y else y

# The largest between the second pair
large_number2 = z if z > n else n

# Find out the largest number among whole user's input
if large_number > large_number2:
    print(f"{large_number} is the largest number")
else:
    print(f"{large_number2} is the largest number")

# HW Lab 2.5
name = input("Enter your name: ")
name = name.upper()
for letter in name:
    if letter in "AEIOUY":
        continue
    else:
        print(letter)

# HW 2.6.
operation = input("+-/* or exit: ")
while operation != "exit":
    num1, num2 = int(input("Enter a number 1: ")), int(input("Enter a number 2: "))
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        break
    operation = input("+-/* or exit: ")
