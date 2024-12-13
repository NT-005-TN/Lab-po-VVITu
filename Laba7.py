# Лабораторная работа №7: Работа с классами ч.3

# Задание 1: Класс Employee
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.employee_id}"

# Задание 2: Класс Manager
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        Employee.__init__(self, name, employee_id)  # Инициализация базового класса Employee
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}."

    def get_info(self):
        base_info = Employee.get_info(self)  # Вызов метода get_info() базового класса Employee
        return f"{base_info}, Отдел: {self.department}"

# Задание 3: Класс Technician
class Technician(Employee):
    def __init__(self, name, employee_id, specialization):
        Employee.__init__(self, name, employee_id)  # Инициализация базового класса Employee
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание в области {self.specialization}."

    def get_info(self):
        base_info = Employee.get_info(self)  # Вызов метода get_info() базового класса Employee
        return f"{base_info}, Специализация: {self.specialization}"

# Задание 4: Класс TechManager
class TechManager(Manager, Technician):
    def __init__(self, name, employee_id, department, specialization):
        Manager.__init__(self, name, employee_id, department)  # Инициализация Manager
        Technician.__init__(self, name, employee_id, specialization)  # Инициализация Technician
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)
        print(f"{employee.name} добавлен в команду {self.name}.")

    def get_team_info(self):
        team_info = [subordinate.get_info() for subordinate in self.subordinates]
        return f"Команда {self.name}:\n" + "\n".join(team_info) if team_info else "Команда пуста."

# Пример использования классов
if __name__ == "__main__":
    # Создаем сотрудников
    emp1 = Employee("Иван Иванов", 1)
    manager1 = Manager("Светлана Петрова", 2, "Маркетинг")
    technician1 = Technician("Алексей Смирнов", 3, "Электроника")
    tech_manager1 = TechManager("Анна Кузнецова", 4, "IT", "Системное администрирование")

    # Демонстрируем функциональность
    print(emp1.get_info())
    print(manager1.get_info())
    print(manager1.manage_project())
    print(technician1.get_info())
    print(technician1.perform_maintenance())
    
    # Добавляем сотрудников в команду тех. менеджера
    tech_manager1.add_employee(manager1)
    tech_manager1.add_employee(technician1)

    # Вывод информации о команде
    print(tech_manager1.get_team_info())
