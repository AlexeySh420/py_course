num = [1, 2, 3, 4]
new_num = num.copy()
print(new_num)
# new_num = num lead to the same place in memory
print(id(new_num))
removedvalue = num.pop()
print(removedvalue)
del num[-1] #remove specific value
len(num)
num.clear()

#for in range print input append result sort reverse len

# n = int(input())
# type(n)
# userList = []
# for i in range(n):
#     userList.append(int(input()))
# else:
#     result = sum(userList)
#     print("original=",userList)
#     userList.sort()
#     print("sorted=", userList)
#     userList.reverse()
#     print("reversed=", userList)
#     print("len=", len(userList))
#     print("sum=", n)

#by value
li = [1, 2, 3, 4, 5,]

for value in li:
    print(value, end=' ')

for index in range(len(li)):
    print("index: ", index)
    print('value ', li[index])

# enumerate
for i, value in enumerate(li):
    print(i, value)

# zip
currency = ["BYN", "RUB", 'USD', 'EUR']
country = ['Belarus', 'Russia', 'USA', 'France']
list(zip(currency, country))

for curr, countr in list(zip(currency, country)):
    print(curr, countr)

# bubble sort
li3 = [1, 3, 5, 2]
# 5 index 2
# 2 index 3
temp = li[2]
li[2] = li[3]
li[3] = temp
temp = li[1]
li[1] = li[2]
li[2] = temp
li[2], li[3] = li[3], li[2]
li[1], li[2] = li[2], li[1]
print(li3)

#slices
new_list = [3, 5, 67, 88, 4, 6, 78]
print(new_list[2:4])
print(new_list[:4])
print(new_list[2:])

print(4 in new_list)

#set

set_test = {5, 5, 5, 1, 2, 3}
print(set_test)

set_test = new_list
new_list = set_test


#list comprehension

st = "strgrghtjo"
li5 = []

# for char in st:
#     if char in 'aeyoiuq':
#         li5.append(char.upper())
#     else:
#         li.append(char*3)

#char.upper() for char in st if char in 'aeyoiuq'

#list in list
li11 = [[1, 2], [2, 3], [3,4], [4,]]
li11[0]
li11[2]
print(li11[0][1])