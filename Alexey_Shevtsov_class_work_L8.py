try:
    cash = int(input("Sum you want to safe: "))
    m = int(input("Months: "))
    res = cash / m
    print(f"You need to safe {res} for {m} months for {cash}")
except ZeroDivisionError:
    print("Please use positive integers")
except ValueError:
    print("Can't convert strings into integers")
except:
    print("Invalid input")

try:
    cash = int(input("Sum you want to safe: "))
    m = int(input("Months: "))
    res = cash / m
    print(f"You need to safe {res} for {m} months for {cash}")
except ZeroDivisionError as e:
    print("Please use positive integers")
    print(e)
    print(e.args)
    print(e.with_traceback)
except ValueError as e:
    print("Can't convert strings into integers")
    print(e)
    print(e.args)
    print(e.with_traceback)
except BaseException as e:
    print("Base")
except:
    print("Invalid input")

raise ZeroDivisionError

# 15.04.2026
