# deepcopy
import copy
inner_list = [4, 3, 2]
outer_list = [1, 2, 3, inner_list, 5]
c2 = copy.deepcopy(outer_list)
# lazy copy
c1 = outer_list.copy()
print(c1)
print(c2)

# Strings
#print index and value
s = "abcdf"
for index in range(len(s)):
    print(index, s[index])

help(ord) # char's unicode number
help(chr) # char string

for i in s:
    print(i, ord(i))

print(chr(100))

# Notae Caesarianae
message = 'Hello World'
for i in message:
    print(i, ord(i), "    |    ", chr(ord(i) + 5), ord(i)+ 5)
secured_message = ""
for i in message:
    secured_message += chr(ord(i) + 5)
print(secured_message)
key = 5
for i in secured_message:
    print(chr(ord(i) - key), end="")
print('\n')


s2 = 'hello'
text = 'HELLOO'
newHello = s2[:2] + text + s2[4:]
print(newHello)

# in not in
'a' in s
set(s)
list(s)
s.upper()
first_name = "STAS"
first_name.capitalize() # First letter in the string is big
first_name.title() # All first letter in the string are big
first_name.lower()

c = "C"
print(c.isalpha()) # check if alphabetic
print(c.isdigit()) # check if numeral

url = 'hotmail.*'
list5 = ["com", "ru", "by"]
urlList = []
for postfix in list5:
    for i in list5:
        urlList.append(url.replace("*", postfix))
print(urlList)

s.rstrip()

# 01.04.2026