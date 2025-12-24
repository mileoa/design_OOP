from abc import ABC, abstractmethod


class AnimalATD(ABC):

    @abstractmethod
    def __init__(self, name: str):
        """
        Создает животного с указанным именем
        """

    @abstractmethod
    def make_sound(self) -> str:
        """
        Постусловие: возвращает звук животного
        """


# Наследование с конкретизацией (reification inheritance)
class Dog(AnimalATD):

    def __init__(self, name: str):
        self._name: str = name

    def make_sound(self) -> str:
        return "Woof"


# Наследование с функциональной вариацией (functional variation inheritance)
class Puppy(Dog):

    def make_sound(self) -> str:
        return "Yap"


# Наследование с вариацией типа (type variation inheritance)
class FamousSpekingDog(Dog):

    def make_sound(self, sound: str) -> str:
        return sound


# Структурное наследование (structure inheritance)
class Movable:
    def move(self) -> None:
        print("Moved")


class BusyPuppy(Movable, Dog):
    pass
