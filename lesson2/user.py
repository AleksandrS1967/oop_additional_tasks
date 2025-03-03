"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:

    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.is_adm = False
        self._is_adm = False
        self._is_logged_in = True

    @property  #
    def name(self):
        return self.__name

    @property  #
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def is_admin(self):
        return self.is_adm

    @is_admin.setter
    def is_admin(self, new):
        self.is_adm = new

    @property
    def _is_admin(self):
        return self.is_admin

    @_is_admin.setter
    def _is_admin(self, new):
        self.is_admin = new

    def login(self, password):
        if password == self.__password:
            print(True)
        else:
            print(False)

    def logout(self):
        self._is_logged_in = not self._is_logged_in
        print(self._is_logged_in)






# код для проверки 
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()

