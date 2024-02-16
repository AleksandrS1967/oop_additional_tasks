"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""
#
#
# class MyList2:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         self.__iterator = 0
#         return self
#
#     def __next__(self):
#         if self.__iterator < len(self.data):
#             self.__iterator += 1
#             return self.__iterator
#         else:
#             raise StopIteration
#
#     def __getitem__(self, index):
#         return self.data[index]
#
#
#
# # код для проверки
# my_list = MyList2([1, 2, 3])
# for i in my_list:
#     print(i, 'my_list', end=', ', sep='/')  # 1 2 3
#
# print(f'\n{my_list[1]}')  # 2
class A:
    def __init__(self):
        self.b =(' ')

    def __call__(self, args):
        return self.b.append(args)

g = A()

gk = ['ergergw']
k = g(gk)

print(k)