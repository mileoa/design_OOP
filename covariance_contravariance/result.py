from typing import Callable


class Animal:

    def eat(self) -> None:
        print("Eat")


class Dog(Animal):

    def play(self) -> None:
        print("Play")


class Puppy(Dog):

    def play_with_tail(self) -> None:
        print("play_with_tail")


# Ковариантность
animals: list[Animal] = [Dog(), Puppy()]
for animal in animals:
    animal.eat()


# Контравариантность
def animal_action(animal: Animal) -> None:
    animal.eat()


def dog_action(dog: Dog) -> None:
    dog.play()


def puppy_action(puppy: Puppy) -> None:
    puppy.play()


animal_action(Animal())
animal_action(
    Dog()
)  # Действия применимые к dog, могут быть применены к animal.
animal_action(
    Puppy()
)  # Действия применимые к puppy, могут быть применены к animal.

dog_action(
    Animal()
)  # Так нельзя, действия применимые к dog, не могут быть применимы к animal.
dog_action(Dog())
dog_action(Puppy())  # действия применимые к puppy, могут быть применимы к dog.

puppy_action(Puppy())
puppy_action(
    Dog()
)  # Так нельзя, действия применимые к puppy, не могут быть применимы к dog.
