# تعريف الفئة
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof! My name is " + self.name

# إنشاء كائن
my_dog = Dog("Buddy", "Golden Retriever")

# الوصول إلى الخصائص والطرق
print(my_dog.name)
print(my_dog.breed)
print(my_dog.bark())
