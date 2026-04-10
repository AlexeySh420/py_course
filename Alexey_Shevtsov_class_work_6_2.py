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