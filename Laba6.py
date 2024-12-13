# Лабораторная работа №6: Работа с классами ч.2

# Задание 1: Защита данных пользователя
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Приватный атрибут

    def set_password(self, new_password):
        # Метод для безопасной смены пароля
        self.__password = new_password
        print("Пароль успешно изменен.")

    def check_password(self, password):
        # Метод для проверки пароля
        return self.__password == password

# Пример использования класса UserAccount
user = UserAccount("user123", "user@example.com", "securepassword")
print(f"Имя пользователя: {user.username}, Электронная почта: {user.email}")

# Изменяем пароль
user.set_password("newsecurepassword")

# Проверяем новый пароль
is_correct = user.check_password("newsecurepassword")
print(f"Пароль верный: {is_correct}")

# Проверяем неверный пароль
is_correct = user.check_password("wrongpassword")
print(f"Пароль верный: {is_correct}")

# Задание 2: Полиморфизм и наследование
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)  # Вызов конструктора базового класса
        self.fuel_type = fuel_type

    def get_info(self):
        # Переопределяем метод get_info
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"

# Пример использования классов Vehicle и Car
vehicle = Vehicle("Toyota", "Camry")
print(vehicle.get_info())

car = Car("Honda", "Civic", "Бензин")
print(car.get_info())
