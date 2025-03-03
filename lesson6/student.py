"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:

    def __init__(self, name, course, grades):
        self.name = name
        self.course = course
        self.grades = grades

    def avg_rate(self):
        b = 0
        if sum(self.grades) == b:
            print(float(b))
        try:
            print(sum(self.grades)/len(self.grades))
        except ZeroDivisionError:
            print(ZeroDivisionError('на ноль делить нельзя'))


#код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate() # 4.75

student = Student('Ivan', 'Python', [])
student.avg_rate() # 0.0
