import copy
import pickle
from abc import ABC, abstractmethod


class General(object):

    def copy_form(self, object: "General") -> None:
        for key, value in self.__dict__.items():
            setattr(self, key, value)

    def deep_copy(self, object: "General"):
        object_copy = copy.deepcopy(self)
        for key, value in object_copy.__dict__.items():
            setattr(self, key, value)

    def clone(self) -> "General":
        return copy.deepcopy(self)

    # Сравнение делается через магический метод __eq__ и уже реализован в object

    def serialize(self) -> bytes:
        return pickle.dumps(self)

    def deserialize(self, object: bytes) -> None:
        obj = pickle.loads(object)
        self.__dict__.update(obj.__dict__)

    # печать (наглядное представление содержимого объекта в текстовом формате); Реализовано в object.__repr__

    def is_eq_type(self, object: "General") -> bool:
        return isinstance(self, type(object))

    # получение реального типа объекта (непосредственного класса, экземпляром которого он был создан).
    def get_type(self):
        return type(self)


class Any(General):
    pass


class Animal(ABC, General):

    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Void(Any, Animal):

    def make_sound(self):
        return ""


def demonstrate_polymorphism(animal: Animal):
    print(f"Animal name: {animal.name}")
    print(f"Sound: {animal.make_sound()}")


dog = Dog("Buddy")
cat = Cat("Whiskers")
void_animal = Void("Placeholder")

# Полиморфное использование
demonstrate_polymorphism(dog)
demonstrate_polymorphism(cat)
demonstrate_polymorphism(void_animal)
