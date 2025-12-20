from typing import List, TypeVar


T_co = TypeVar("T_co", covariant=True)


class Animal:
    def make_sound(self) -> str:
        return ""


class Dog(Animal):
    def make_sound(self) -> str:
        return "Гав!"

    def fetch(self) -> str:
        return "Принес палку!"


# animaobjects  используется и как полиморфный объект, и в ковариантном вызове
def problematic_function(objects: List[T_co]) -> List[str]:
    result: List[str] = []
    for o in objects:
        result.append(o.fetch())
    return result


# x участвует в полиморфном присваивании
x: List[Animal] = [Dog(), Dog(), Animal()]

problematic_function(x)  # x используется как параметр метода
