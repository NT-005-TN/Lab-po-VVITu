# Лабораторная работа №2: Функции в Python и базовые алгоритмы

# Задание 1: Написание простых функций

# Функция greet, которая принимает имя пользователя и выводит приветствие
def greet(name):
    print(f"Привет, {name}!")

# Функция square, которая возвращает квадрат переданного числа
def square(number):
    return number ** 2

# Функция max_of_two, которая возвращает большее из двух чисел
def max_of_two(x, y):
    return x if x > y else y

# Примеры использования функций из задания 1
greet("Алексей")
print("Квадрат числа 5:", square(5))
print("Большее число между 10 и 20:", max_of_two(10, 20))


# Задание 2: Работа с аргументами функций

# Функция describe_person, принимающая имя и возраст человека
def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")

# Примеры использования функции из задания 2
describe_person("Мария")
describe_person("Иван", 25)


# Задание 3: Использование функций для решения алгоритмических задач

# Функция is_prime, которая определяет, является ли число простым
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Примеры использования функции из задания 3
print("Число 7 простое:", is_prime(7))
print("Число 10 простое:", is_prime(10))
