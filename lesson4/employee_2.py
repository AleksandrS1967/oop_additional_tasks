"""
Для класса Employee, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:

    def __init__(self, pay):
        self.pay = int(pay)

    def __add__(self, other):
        self.pay += int(other.pay)
        return int(self.pay)


class Client:

    def __init__(self, pay):
        self.pay = pay

    # def __add__(self, other):
    #     self.pay += int(other.pay)
    #     return int(self.pay)


class Developer(Employee):
    pass


class Manager(Employee):
    pass

# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    if isinstance(user, Employee):
        total_salary = total_salary + user.pay

print(total_salary)
# Вывод: 150000
