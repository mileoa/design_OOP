from abc import abc, abstractmethod
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


# Расширение класса-родителя (наследник задаёт более общий случай родителя).
class Box(Generic[T]):

    def __init__(self):
        self._storage: list[T] = []
        print("Коробка")

    def store(self, item: T) -> None:
        self._storage.append(item)


class BoxlikeStorage(Box, Generic[T]):
    def __init__(self):
        super().__init__()
        print("Коробкообразное хранилище, хранилище похожее на коробку")


# Специализация класса-родителя (наследник задаёт более специализированный случай родителя).
class Car:
    def __init__(self):
        print("Машина")


class TurboCar(Car):

    def __init__(self):
        super().__init__()
        print("Машина")

    def turbo(self) -> None:
        print("Включить турбо")


# Комбинация нескольких родительских классов.
class Printable(abc):

    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Clickable(abc):

    def __init__(self):
        pass

    @abstractmethod
    def set_action_for_click(self, action: Callable):
        pass

    @abstractmethod
    def click(self):
        pass


class Button(Printable, Clickable):

    def __init__(self):
        super().__init__()
        self._action_for_click: Callable = lambda: None
        print(
            "Кнопка отображается и на нее можно нажать"
            " для выполнения какого-либо дейтсвия"
        )

    def draw(self) -> None:
        print("Отображение кнопки")

    def set_action_for_click(self, action: Callable) -> None:
        self._action: Callable = action

    def click(self) -> None:
        self._action()
