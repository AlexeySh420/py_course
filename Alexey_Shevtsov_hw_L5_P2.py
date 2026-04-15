# Homework 5.0.
def main():
    operation = input("Select operation +,-,/,*,exit: ")

    while operation != "exit":
        num1, num2 = int(input("Enter a number 1: ")), int(input("Enter a number 2: "))
        if operation == "+":
            add(num1, num2)
        elif operation == "-":
            subtract(num1, num2)
        elif operation == "*":
            multiply(num1, num2)
        elif operation == "/":
            divide(num1, num2)
        else:
            break
        operation = input("+-/* or exit: ")


def add(num1, num2):
    """
    Adds two numbers
    """
    return num1 + num2


def subtract(num1, num2):
    """
    Subtract two numbers
    """
    return num1 - num2


def multiply(num1, num2):
    """
    Multiply two numbers
    """
    return num1 * num2


def divide(num1, num2):
    """
    Divide two numbers
    """
    return num1 / num2


if __name__ == "__main__":
    main()

# Homework 5.1.
import calendar

def main():
    user_year = int(input("Enter a year: "))
    if year_type(user_year) == True:
        print(f"{user_year} is a leap year")
    else:
        print(f"{user_year} is not a leap year")

def year_type(n):
    return calendar.isleap(n)


if __name__ == "__main__":
    main()

import calendar

def main():
    test_data = [1500, 1900, 2000, 2016, 1987]
    test_results = [False, False, True, True, False]
    for year, result in zip(test_data, test_results):
        if is_year_leap(year) == result:
            print(year, 'is leap? -->', result)
        else:
            print(year, 'from your funct -->', is_year_leap(year))
            print('but expected -->')

def is_year_leap(year):
    """
    Calendar lib checks if the year is a leap year
    """
    return calendar.isleap(year)

if __name__ == "__main__":
    main()

# BMI.
def main():
    user_weight = int(input("Enter your weight: "))
    user_height = float(input("Enter your height: "))

    bmi = round(count_bmi(user_weight, user_height), 2)
    if bmi < 18:
        print(f"Your BMI is {bmi} and you are underweight")
    elif 18 <= bmi < 25:
        print(f"Your BMI is {bmi} and you are normal")
    else:
        print(f"Your BMI is {bmi} and you are overweight")

def count_bmi(weight, height):
    return weight / (height ** 2)

if __name__ == '__main__':
    main()

# Factorial.
def main():
    user_num = int(input("Enter number: "))
    print(factorial(user_num))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    main()

# Homework 5.4.

def main():
    user_input = int(input("Enter number: "))
    febo(user_input)

def febo(n):
    x, y = 0, 1
    for _ in range(n):
        print(x, end=' ')
        x, y = y, x + y

if __name__ == "__main__":
    main()