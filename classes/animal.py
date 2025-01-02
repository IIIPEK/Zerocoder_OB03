class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

    def eat(self):
        return "I am a bird and I eat seeds"
    def __str__(self):
        return f"Bird: {super().__str__()}"

class Mammal(Animal):
    def make_sound(self):
        return "Meow"

    def eat(self):
        return "I am a mammal and I eat meat"

    def __str__(self):
        return f"Bird: {super().__str__()}"


class Reptile(Animal):
    def make_sound(self):
        return "Hiss"

    def eat(self):
        return "I am a reptile and I eat insects"

    def __str__(self):
        return f"Bird: {super().__str__()}"
