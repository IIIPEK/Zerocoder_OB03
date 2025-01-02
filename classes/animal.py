class Animal:
    type = "Animal"
    def __init__(self, name, age,sound=''):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return self.sound

    def eat(self):
        pass

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Bird(Animal):
    type = "Bird"

    def eat(self):
        return "I am a bird and I eat seeds"

    def __str__(self):
        return f"{self.type}: {super().__str__()}"

class Mammal(Animal):
    type = "Mammal"

    def make_sound(self):
        return self.sound

    def eat(self):
        return "I am a mammal and I eat meat"

    def __str__(self):
        return f"{self.type}: {super().__str__()}"


class Reptile(Animal):
    type = "Reptile"

    def make_sound(self):
        return "Hiss"

    def eat(self):
        return "I am a reptile and I eat insects"

    def __str__(self):
        return f"{self.type}: {super().__str__()}"
