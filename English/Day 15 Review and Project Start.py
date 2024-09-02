# Review Concepts with a Small Project

# Define a Class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 60


# Create a List of Students
students = [
    Student("Alice", 85),
    Student("Bob", 58),
    Student("Charlie", 70)
]

# Check Which Students Are Passing
for student in students:
    if student.is_passing():
        print(student.name + " is passing.")
    else:
        print(student.name + " is not passing.")
