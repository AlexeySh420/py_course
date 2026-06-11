#Phonebook

class PhoneNumberError(Exception):
    def __init__(self, phone, message):
        self.phone = phone
        self.message = message

try:
    raise PhoneNumberError('375880000GF', 'contain not numbers')
except PhoneNumberError as err:
    print(f'{err.phone} --> {err.message}')



class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message
    def __str__(self):
        return f'NumberError: number: {self.number}, message: {self.message}'
    
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'user name: {self.name}.'
    def call(self, number):
        if len(number) < 8:
            raise NumberError(number, 'Number is too short!')
        return f'Calling {number}'

user1 = User('Vasia')
try:
    user1.call('123')
except NumberError as e:
    print(e)
except:
    print('-1')

try:
    user1.call('12345678')
except NumberError as e:
    print(e)
except:
    print('-1')
        