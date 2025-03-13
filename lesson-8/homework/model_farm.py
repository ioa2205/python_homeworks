# Model a Farm

class Animal:
    def __init__(self, name, age, species, sound):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child Classes
class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cow", "Moo")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken", "Cluck")

    def lay_egg(self):
        print(f"{self.name} laid an egg!")

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Sheep", "Baa")

    def shear(self):
        print(f"{self.name} is being sheared for wool.")

# Creating farm animals
cow = Cow("Bessie", 4)
chicken = Chicken("Clucky", 2)
sheep = Sheep("Dolly", 3)

# Demonstrating behaviors
cow.make_sound()
cow.eat("grass")
cow.produce_milk()

chicken.make_sound()
chicken.lay_egg()

sheep.make_sound()
sheep.shear()
