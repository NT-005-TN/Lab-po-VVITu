# Лабораторная работа №3: Работа с файлами в Python: открытие, чтение, запись, работа с исключениями

# Задание 1: Открытие и чтение файла

# Функция для чтения файла
def read_file(file_name, read_type='all'):
    try:
        with open(file_name, 'r') as file:
            if read_type == 'all':
                content = file.read()
                print(content)
            elif read_type == 'line':
                for line in file:
                    print(line, end='')  # end='' чтобы не добавлять лишний перевод строки
            else:
                print("Неверный тип чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

# Пример использования функции
read_file('example.txt', 'all')  # Чтение всего файла
read_file('example.txt', 'line')  # Построчное чтение


# Задание 2: Запись в файл

# Функция для записи текста в файл
def write_to_file(file_name, text, append=False):
    mode = 'a' if append else 'w'  # 'a' для добавления, 'w' для записи
    with open(file_name, mode) as file:
        file.write(text + '\n')  # Добавляем перевод строки после текста

# Запрашиваем текст у пользователя и записываем в файл
user_input = input("Введите текст для записи в файл user_input.txt: ")
write_to_file('user_input.txt', user_input)

# Пример добавления текста в существующий файл
additional_input = input("Введите текст для добавления в файл user_input.txt: ")
write_to_file('user_input.txt', additional_input, append=True)


# Задание 3: Обработка исключений

# Модифицированная функция для чтения файла с обработкой исключений
def read_file_with_exception_handling(file_name, read_type='all'):
    try:
        with open(file_name, 'r') as file:
            if read_type == 'all':
                content = file.read()
                print(content)
            elif read_type == 'line':
                for line in file:
                    print(line, end='')  # end='' чтобы не добавлять лишний перевод строки
            else:
                print("Неверный тип чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден. Пожалуйста, проверьте имя файла и попробуйте снова.")

# Пример использования функции с обработкой исключений
read_file_with_exception_handling('non_existent_file.txt', 'all')  # Пробуем открыть несуществующий файл
