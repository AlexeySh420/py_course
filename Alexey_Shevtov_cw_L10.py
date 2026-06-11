class Car:
    pass


class Wallet:
    pass


class Animal:
    pass


class User:
    counter = 0  # class variable

    def __init__(self, user_name, user_phone, age, user_email=""):
        self.name = user_name
        self.phone = user_phone
        self.email = user_email
        self.age = age
        User.counter += 1

    # Those methods can be replaced with the default: getattr hasattr setattr
    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def __len__(self):
        return self.age

    def __str__(self):
        return f"name: {self.name} | phone: {self.phone} | age: {self.age} | email: {self.email}"

    def __repr__(self):
        return f" repr: name: {self.name} | phone: {self.phone} | age: {self.age} | email: {self.email}"


mycar = Car()
alexey = User("Alexey", "1234567", "alexey@email.com")

print(alexey.name, alexey.phone, alexey.email)
alexey.phone = "7654321"  # That's how we update it.

print(User.__dict__, "\n", alexey.__dict__)


# Inheritance
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f" repr: name: {self.name} | age: {self.age}"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __add__(self, another_dog):
        return self.age + another_dog.age


class Bulldog(Dog):
    def walk(self, steps):
        return f"{self.name} walks {steps}"

    # Enhanced method from the parent Class (Method Overwriting).
    def speak(self, sound):
        par_speak = super().speak(sound)
        par_speak = par_speak.upper()
        return "Bulldog speak\n" + par_speak
        # return "Bulldog barks\n" + super().speak(sound)


jimmy = Bulldog("Jimmy", "6")
print(jimmy.speak("Woof"))
print(jimmy.walk(63664364))
print(jimmy.speak("OTF"))

print(Bulldog.__bases__)


class Terrier(Dog):
    def __init__(self, name, age, color):
        # self.___color = color # way to hide an atribute
        self.color = color
        super().__init__(name, age)

    def __repr__(self):
        return super().__repr__() + f" |color:{self.color}"


kelly = Terrier("Kelly", "6", "blue")

# Queue

# fifo 1 2 3 4 5 6
# stack (lifo)

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