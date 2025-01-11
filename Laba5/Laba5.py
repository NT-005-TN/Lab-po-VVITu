# Лабораторная работа №5: Работа с классами

# Задание 1: Класс Book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

# Пример использования класса Book
book1 = Book("1984", "Джордж Оруэлл", 1949)
print(book1.get_info())

# Задание 2: Класс Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

# Пример использования класса Circle
circle1 = Circle(5)
print(f"Исходный радиус круга: {circle1.get_radius()}")

# Изменяем радиус
circle1.set_radius(10)
print(f"Новый радиус круга: {circle1.get_radius()}")
