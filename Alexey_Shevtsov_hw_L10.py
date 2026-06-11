class Stack:
    def __init__(self):
        self.___storage = []

    def push(self, value):
        self.___storage.append(value)
        print("Adding", value)

    def pop(self):
        try:
            res = self.___storage.pop()
            print("Removing", res)
        except IndexError:
            print("Empty storage")
        except:
            print("Something went wrong")
    def get_stack(self):
        return self.___storage

storage1 = Stack()
storage1.push(10)
storage1.push(20)

storage1.pop() # 20
storage1.pop() # 10



# Mobile Phone
class MobilePhone():
    def __init__(self, number):
        self.number = number
        self.switch = False

    def turn_on(self):
        self.switch = True
        return f'mobile phone {self.number} is enabled'
    
    def turn_off(self):
        self.switch = False
        return f'mobile phone {self.number} is turned off'
    
    def call(self, cally):
        if self.switch:
            return f'calling {cally}'
        else:
            return f'The phone is off'



phone1 = MobilePhone('3752900770007')
phone2 = MobilePhone('375330011001')

print(phone1.turn_on())
print(phone2.turn_on())

print(phone2.call('2889933'))

print(phone1.turn_off())
print(phone2.turn_off())