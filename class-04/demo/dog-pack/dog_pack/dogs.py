from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod


class Dog(ABC):

    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        self.__class__.increase_count()

    def sleep(self):
        return "zzz"

    @abstractclassmethod
    def increase_count(cls):
        Dog.count += 1

    @abstractmethod
    def greet(self):
        pass

    @abstractstaticmethod
    def get_characteristics():
        pass

    @classmethod
    def get_all_dog_count(cls):
        return cls.count


class Boxer(Dog):
    """
    A super cool dog
    """

    count = 0

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return super().increase_count()

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    @staticmethod
    def get_characteristics():
        return "Boxers are lovers, not fighters."

    @classmethod
    def get_breed_count(cls):
        return cls.count


class Puggle(Dog):
    """
    adorably spunky
    """

    count = 0

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return super().increase_count()

    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"

    @classmethod
    def get_breed_count(cls):
        return cls.count
