
# an idea or notion of a Dog
# attributes e.g. fur color
# actions e.g lick the fur

# Dog is a idea, template, recipe
# in JS think Constructors

# a particular dog, e.g. Mama Lela is an "instance" of a Dog


class Pet:
    def __init__(self, name):
        self.name = name
        self.destroy_preface = 'I really like to destroy'

    def __repr__(self):
        return '???:' + self.name

    def __str__(self):
        return f'I am a ??? named {self.name}'

    def speak(self):
        return '????'

    def destroy(self):
        return f'{self.destroy_preface} {self.__class__.target_of_destruction}'



class Dog(Pet):

    target_of_destruction = 'tables'

    def __repr__(self):
        return 'Dog:' + self.name

    def __str__(self):
        return f'I am a Dog named {self.name}'

    # def destroy(self):
    #     return f'{self.destroy_preface} {self.__class__.target_of_destruction}'

    # def speak(self):
    #     return 'Woof'


class Cat(Pet):

    target_of_destruction = 'sofa'

    def __repr__(self):
        return 'Cat:' + self.name

    def __str__(self):
        return f'I am a Cat named {self.name}'

    def speak(self):
        return 'Meow'


    # def destroy(self):
    #     return f'{self.destroy_preface} {self.__class__.target_of_destruction}'


cat = Cat('Kerfuffle')
dog = Dog('Karma')

print(cat.destroy())
print(dog.destroy())
