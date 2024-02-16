"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    __slots__ = ('name', 'age', 'grades')

    def __init__(self):
        self.name = ' '
        self.age = 0
        self.grades = []

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.grades}'


class Course:
    __slots__ = ('name', 'students')

    def __init__(self):
        self.name = ' '
        self.students = []

    def __repr__(self):
        return f'{self.name}, {self.students}'


# код для проверки 
student1 = Student()
student1.name = "John"
print(student1.name)
student1.age = 20
print(student1.age)
student1.grades = [90, 80, 85]
print(student1.grades)

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]
print(student2.name)
print(student2.age)
print(student2.grades)

course = Course()
course.name = "Math"
course.students = [student1, student2]

print(course.name)
print(course.students)
