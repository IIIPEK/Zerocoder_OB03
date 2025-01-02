"""
1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
"""

from classes.animal import Bird, Mammal, Reptile
from classes.employee import ZooKeeper, Veterinarian
from classes.zoo import Zoo

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

zoo = Zoo()
zoo.read_lists()

if not zoo.animal_exists("Pigeon"):
    zoo.add_animal(Bird("Pigeon", 2, "Chirp"))
if not zoo.animal_exists("Lion"):
    zoo.add_animal(Mammal("Lion", 5))
if not zoo.animal_exists("Snake"):
    zoo.add_animal(Reptile("Snake", 3))

if  not zoo.employee_exists("John"):
    zoo.add_employee(ZooKeeper("John", 30, 5000))
if not zoo.employee_exists("Jane"):
    zoo.add_employee(Veterinarian("Jane", 25, 6000))

zoo.list_animals()
zoo.list_employees()

zoo.update_lists()
animal_sound(zoo.get_animals())

aimals=zoo.get_animals()

for animal in aimals:
    zoo.get_zookeepers()[0].feed_animal(animal)

for animal in aimals:
    zoo.get_veterinarians()[0].heal_animal(animal)

