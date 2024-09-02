# مراجعة المفاهيم بمشروع صغير

# تعريف الفئة
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 60


# إنشاء قائمة بالطلاب
students = [
    Student("Alice", 85),
    Student("Bob", 58),
    Student("Charlie", 70)
]

# التحقق من الطلاب الناجحين
for student in students:
    if student.is_passing():
        print(student.name + " ناجح.")
    else:
        print(student.name + " غير ناجح.")
