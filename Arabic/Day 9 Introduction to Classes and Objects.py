# Class Definition
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof! My name is " + self.name


# Creating an Object
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing Attributes and Methods
print(my_dog.name)
print(my_dog.breed)
print(my_dog.bark())
