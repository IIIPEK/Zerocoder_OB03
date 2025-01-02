from classes.animal import Bird, Mammal, Reptile
from classes.employee import ZooKeeper, Veterinarian
from classes.datahandler import DataHandler

class Zoo:
    def __init__(self):
        self.data_handler = DataHandler("zoo.db")
        self.data_handler.create_table('animals', ['type TEXT','name TEXT', 'age INTEGER', 'sound TEXT'])
        self.data_handler.create_table('employees', ['type TEXT','name TEXT', 'age INTEGER', 'salary INTEGER', 'position TEXT'])
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_animals(self):
        return self.animals

    def get_employees(self):
        return self.employees

    def list_animals(self):
        for animal in self.animals:
            print(animal)

    def list_employees(self):
        for employee in self.employees:
            print(employee)

    def get_zookeepers(self):
        return [employee for employee in self.employees if isinstance(employee, ZooKeeper)]

    def get_veterinarians(self):
        return [employee for employee in self.employees if isinstance(employee, Veterinarian)]

    def update_lists(self):
        self.data_handler.delete_data('animals')
        self.data_handler.delete_data('employees')

        for animal in self.animals:
            self.data_handler.insert_data('animals', [animal.type, animal.name, animal.age, animal.sound])

        for employee in self.employees:
            self.data_handler.insert_data('employees', [employee.type, employee.name, employee.age, employee.salary, employee.position])

    def read_lists(self):
        self.animals = []
        animals = self.data_handler.get_data('animals')
        for animal in animals:
            if animal[0] == 'Bird':
                self.animals.append(Bird(animal[1], animal[2], animal[3]))
            elif animal[0] == 'Mammal':
                self.animals.append(Mammal(animal[1], animal[2], animal[3]))
            elif animal[0] == 'Reptile':
                self.animals.append(Reptile(animal[1], animal[2], animal[3]))

        self.employees = []
        employees = self.data_handler.get_data('employees')
        for employee in employees:
            if employee[0] == "Zoo Keeper":
                self.employees.append(ZooKeeper(employee[1], employee[2], employee[3]))
            elif employee[0] == "Veterinarian":
                self.employees.append(Veterinarian(employee[1], employee[2], employee[3]))



    def animal_exists(self, name):
        for animal in self.animals:
            if animal.name == name:
                return True
        return False

    def employee_exists(self, name):
        for employee in self.employees:
            if employee.name == name:
                return True
        return False
