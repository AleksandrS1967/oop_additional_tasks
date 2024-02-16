"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:
    __slots__ = ('brend', 'model', 'yar')

    def __init__(self, brend, model, yar):
        self.brend = brend
        self.model = model
        self.yar = yar

    def get_set_del(self):
        self.brend = 'jfuv'
        self.yar = 14589
        del self.brend
        return self.model


class CarSlots:
    def __init__(self, brend, model, yar):
        self.brend = brend
        self.model = model
        self.yar = yar

    def get_set_del(self):
        self.brend = 'jfuv'
        self.yar = 14589
        del self.brend
        return self.model


car = Car('Toyota', 'Corolla', 2022)
print(car.get_set_del())
car_slots = Car('Toyota', 'Crown', 1990)
print(car_slots.get_set_del())

import timeit

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)
print((t1-t2)/t1*100)
print(t1, 2)
print(t2, 1)
