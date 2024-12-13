# main_package.py

# Импортируем модули из пакета
from my_package import math_operations, string_operations

# Используем функции из модулей
product = math_operations.multiply(4, 5)
print(f"Произведение 4 и 5 равно {product}")

combined_string = string_operations.concatenate("Hello, ", "world!")
print(f"Результат конкатенации: {combined_string}")
