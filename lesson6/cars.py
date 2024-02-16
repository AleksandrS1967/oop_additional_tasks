"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""


class Car:
    def __init__(self, name, model, yea):
        self.name = name
        self.model = model
        self.yea = yea
        # if self.yea > 2024:
        """первый вариант решения"""
        #     raise Exception("raises Exception('Эта машина еще не была выпущена')")



# код для проверки
car = Car('Toyota', 'Corolla', 2022)
#print(car.yea)
#car1 = Car('Toyota', 'Corolla', 3000)
try:
    """второй вариант решения"""
    car = Car('Toyota', 'Corolla', 3000)
    if car.yea > 2024:
        print(Exception("raises Exception('Эта машина еще не была выпущена')"))
except Exception:
    raise (Exception("raises Exception('Эта машина еще не была выпущена')"))
# raises Exception('Эта машина еще не была выпущена')
