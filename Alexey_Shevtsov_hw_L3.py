# HW 3.1.
hat_list = [1, 2, 3, 4, 5]
print(len(hat_list))
user_input = input("Enter a number: ")
hat_list[2] = user_input
hat_list.pop()
print(len(hat_list))
print(hat_list)

# HW 3.3.
li = []
count = int(input("How many numbers you got? "))
while len(li) != count:
    x = li.append(int(input("Please enter a number: ")))

swapped = True
while swapped:
    swapped = False
    for index in range(len(li) - 1):
        if li[index] > li[index + 1]:
            swapped = True
            li[index], li[index + 1] = li[index + 1], li[index]
print(li)

# HW 3.4.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
res_list = sorted(set(my_list))
res_list = list(res_list)
print(res_list)

# HW 3.5.
user_input = input("enter numbers: ").split()
li = [int(i) for i in user_input]
print(sum(li))
