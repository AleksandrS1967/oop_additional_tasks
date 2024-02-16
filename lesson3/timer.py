"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from datetime import datetime as dt


class Timer:
    elapsed_time = dt.now()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.elapsed_time = (dt.now() - self.elapsed_time)
        # print(self.elapsed_time)
        # b = dt.now()
        # c = b - self.elapsed_time
        # self.elapsed_time = c
        # print(c.microseconds)


with Timer() as timer:
    count = 0
    for i in range(0, 1000000):
        count += i
    b = dt.now()
    timer.elapsed_time = b - timer.elapsed_time


    # код для проверки
    print("Execution time:", timer.elapsed_time)
