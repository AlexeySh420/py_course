# L13 04.27.2026
file_obj = open('users.txt', 'rt', encoding='utf-8') 
type(file_obj)
new_file_obj = open('users2.txt', 'wt', encoding='utf-8')



strings = file_obj.readlines()
strings.append(11111111)
print(strings)

file_obj.close()
new_file_obj.close()

my_file_obj = open('test.txt', 'wt', encoding='utf-8')
test_list = [ 'test', 'test', 'test', 'test']
res_list = []
sep ='\n'
for string in test_list:
    res_list.append(string + sep)

my_file_obj.writelines(test_list)
my_file_obj.close

my_file_obj=open('test1.txt', 'wt', encoding='utf-8')
my_file_obj.writelines(res_list)
my_file_obj.close()



s_number = int(input('How many lines you want to enter into the file? --> '))
my_file_obj1 = open('interactive.txt', 'wt', encoding='utf-8')

for i in range(s_number):
    my_file_obj1 = open('interactive.txt', 'at', encoding='utf-8')
    user_text = input('Enter a plain text --> ')
    user_text += f' number of iteration {sep}' #sep ='\n'
    my_file_obj1.write(user_text)
    my_file_obj1.close()



with open('with_test.txt', 'wt', encoding='utf-8') as my_file_obj3: # it is the same as the examples above
    my_file_obj3.write('This is a test')



import pickle

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'user: {self.name} {self.age}'
    def __repr__(self):
        return f'user: {self.name} {self.age}'
    
d1 = User('D', 10)
d2 = User('C', 15)

with open('data_pickle.txt', 'wb') as fs:
    pickle.dump(d1,fs)

# with open('data_pickle.txt', 'wb') as fs:
#     new_d1 = pickle.load(fs)



# xml 
import xml.etree.ElementTree as et

tree = et.parse('books.xml')
root_element = tree.getroot()

type(root_element)
print(root_element.tag)
print(root_element.text)
print(root_element.tail)

for sub in root_element:
    print(sub.tag, sub.attrib)

for sub in root_element:
    print(sub.tag, sub.get('title'))
    for su_sub in sub:
        print(sub.tag, sub.attrib)
    print()
    