class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = None

    def __str__(self):
        return f"{self.position if self.position is not None else 'Employee'} {self.name}, Age: {self.age}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employee(name='{self.name}', age={self.age}, salary={self.salary}, position={self.position})"

class ZooKeeper(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.position = "Zoo Keeper"

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")
        print(animal.eat())

class Veterinarian(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.position = "Veterinarian"

    def heal_animal(self, animal):
        print(f"{self.name} is treating the disease in {animal.name}")
        print(animal.make_sound())

