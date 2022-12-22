# IS a, vs. HAS a
# inheritance vs. composition
class DogPack:
    def __init__(self, dogs=None):
        self.dogs = dogs or []

    def __str__(self):
        dog_strings = [str(dog) for dog in self.dogs]
        # dog_strings = []
        # for dog in self.dogs:
        #     dog_strings.append(str(dog))
        return " ".join(dog_strings)

    def __repr__(self):
        return f"DogPack({self.dogs})"


# base class
class Dog:
    def __init__(self, name):
        self.name = name


# derived class
class Boxer(Dog):
    def __init__(self, name="unknown", jump=0):
        self.name = name
        self.jump = jump

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Boxer('{self.name}')"

    def greet(self):
        return f"The name's {self.name}. Pleasure."


# derived class
class Puggle(Dog):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Puggle('{self.name}')"

    def greet(self):
        return f"My name is! {self.name}.So happy to meet you!"

