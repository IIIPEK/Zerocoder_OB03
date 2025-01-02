from classes.animal import Bird, Mammal, Reptile
from classes.employee import ZooKeeper, Veterinarian

class Zoo:
    def __init__(self):
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